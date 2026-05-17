#!/usr/bin/env python3
"""Simple full-text search over data/processed/chunks.jsonl.

Usage:
    python scripts/search.py "ReAct agenti tool use"
    python scripts/search.py "retrieval budget" --vendor openai --top-k 5
    python scripts/search.py "long context XML" --topic long_context --json
"""
from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path
from typing import Any

TOKEN_RE = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9_]+", re.UNICODE)


def tokenize(text: str) -> list[str]:
    return [t.lower() for t in TOKEN_RE.findall(text or "")]


def load_chunks(path: Path) -> list[dict[str, Any]]:
    chunks: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                chunks.append(json.loads(line))
    return chunks


def build_doc_text(chunk: dict[str, Any]) -> str:
    fields = [
        chunk.get("vendor", ""),
        chunk.get("heading", ""),
        chunk.get("topic", ""),
        " ".join(chunk.get("techniques", []) or []),
        " ".join(chunk.get("use_cases", []) or []),
        chunk.get("text", ""),
        chunk.get("source_ref", ""),
    ]
    return " ".join(fields)


def score_chunk(query: str, chunk: dict[str, Any]) -> float:
    q_tokens = tokenize(query)
    if not q_tokens:
        return 0.0

    text = build_doc_text(chunk)
    text_lower = text.lower()
    d_tokens = tokenize(text)
    if not d_tokens:
        return 0.0

    counts: dict[str, int] = {}
    for t in d_tokens:
        counts[t] = counts.get(t, 0) + 1

    score = 0.0
    unique_q = set(q_tokens)
    for token in unique_q:
        tf = counts.get(token, 0)
        if tf:
            score += 1.0 + math.log(tf)

    # Give extra weight to exact phrase and metadata matches.
    if query.lower() in text_lower:
        score += 4.0
    heading = (chunk.get("heading") or "").lower()
    topic = (chunk.get("topic") or "").lower()
    techniques = " ".join(chunk.get("techniques", []) or []).lower()
    for token in unique_q:
        if token in heading:
            score += 1.5
        if token in topic:
            score += 1.2
        if token in techniques:
            score += 1.2

    # Slight normalization to avoid very long chunks dominating.
    return score / math.sqrt(len(set(d_tokens)) + 1)


def main() -> int:
    parser = argparse.ArgumentParser(description="Search AI docs repository chunks.")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--chunks", default=None, help="Path to chunks.jsonl")
    parser.add_argument("--vendor", default=None, help="Filter by vendor, e.g. openai")
    parser.add_argument("--topic", default=None, help="Filter by topic, e.g. agents")
    parser.add_argument("--top-k", type=int, default=5, help="Number of results")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    chunks_path = Path(args.chunks) if args.chunks else root / "data" / "processed" / "chunks.jsonl"
    chunks = load_chunks(chunks_path)

    if args.vendor:
        chunks = [c for c in chunks if (c.get("vendor") or "").lower() == args.vendor.lower()]
    if args.topic:
        chunks = [c for c in chunks if (c.get("topic") or "").lower() == args.topic.lower()]

    scored = []
    for chunk in chunks:
        score = score_chunk(args.query, chunk)
        if score > 0:
            scored.append((score, chunk))
    scored.sort(key=lambda x: x[0], reverse=True)
    results = scored[: max(args.top_k, 1)]

    if args.json:
        print(json.dumps([
            {"score": round(score, 4), **chunk} for score, chunk in results
        ], ensure_ascii=False, indent=2))
        return 0

    if not results:
        print("No matching chunks found.")
        return 0

    for i, (score, chunk) in enumerate(results, start=1):
        techniques = ", ".join(chunk.get("techniques", []) or [])
        print(f"{i}. [{score:.3f}] {chunk.get('vendor')} - {chunk.get('heading')}")
        print(f"   Topic: {chunk.get('topic')} | Techniques: {techniques}")
        print(f"   {chunk.get('text')}")
        print(f"   Source: {chunk.get('source_ref')}")
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
