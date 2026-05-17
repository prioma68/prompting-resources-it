#!/usr/bin/env python3
"""Create an evidence pack for cross-source comparison.

This script does not call an LLM and does not generate the final interpretation.
It retrieves relevant chunks and organizes them into a structured evidence pack
that can be inspected manually or passed to a grounded LLM workflow.

Examples:
    python scripts/compare_sources.py "prompting bias limiti confronto fonti" --top-k 12
    python scripts/compare_sources.py "agents tool use ReAct Comet" --vendor google --top-k 8
    python scripts/compare_sources.py "retrieval grounding" --output reports/evidence_pack.md
"""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from search import load_chunks, score_chunk


def filter_chunks(chunks: list[dict[str, Any]], vendor: str | None, topic: str | None) -> list[dict[str, Any]]:
    if vendor:
        chunks = [c for c in chunks if (c.get("vendor") or "").lower() == vendor.lower()]
    if topic:
        chunks = [c for c in chunks if (c.get("topic") or "").lower() == topic.lower()]
    return chunks


def retrieve(query: str, chunks: list[dict[str, Any]], top_k: int) -> list[tuple[float, dict[str, Any]]]:
    scored: list[tuple[float, dict[str, Any]]] = []
    for chunk in chunks:
        score = score_chunk(query, chunk)
        if score > 0:
            scored.append((score, chunk))
    scored.sort(key=lambda item: item[0], reverse=True)
    return scored[: max(top_k, 1)]


def chunk_id(chunk: dict[str, Any]) -> str:
    return str(chunk.get("chunk_id") or "unknown_chunk")


def as_markdown(query: str, results: list[tuple[float, dict[str, Any]]]) -> str:
    vendors = Counter((chunk.get("vendor") or "unknown") for _, chunk in results)
    topics = Counter((chunk.get("topic") or "unknown") for _, chunk in results)

    by_vendor: dict[str, list[tuple[float, dict[str, Any]]]] = defaultdict(list)
    for score, chunk in results:
        by_vendor[str(chunk.get("vendor") or "unknown")].append((score, chunk))

    lines: list[str] = []
    lines.append("# Evidence pack")
    lines.append("")
    lines.append(f"Query: {query}")
    lines.append("")
    lines.append("## Coverage")
    lines.append("")
    lines.append("### Vendors")
    lines.append("")
    for vendor, count in sorted(vendors.items()):
        lines.append(f"- {vendor}: {count}")
    lines.append("")
    lines.append("### Topics")
    lines.append("")
    for topic, count in sorted(topics.items()):
        lines.append(f"- {topic}: {count}")
    lines.append("")

    lines.append("## Retrieved chunks")
    lines.append("")
    for index, (score, chunk) in enumerate(results, start=1):
        techniques = ", ".join(chunk.get("techniques", []) or [])
        use_cases = ", ".join(chunk.get("use_cases", []) or [])
        lines.append(f"### {index}. {chunk.get('vendor')} - {chunk.get('heading')}")
        lines.append("")
        lines.append(f"- score: {score:.3f}")
        lines.append(f"- chunk_id: {chunk_id(chunk)}")
        lines.append(f"- doc_id: {chunk.get('doc_id')}")
        lines.append(f"- topic: {chunk.get('topic')}")
        lines.append(f"- techniques: {techniques}")
        if use_cases:
            lines.append(f"- use_cases: {use_cases}")
        lines.append(f"- source_ref: {chunk.get('source_ref')}")
        lines.append("")
        lines.append("Evidence summary:")
        lines.append("")
        lines.append(str(chunk.get("text") or ""))
        lines.append("")

    lines.append("## Prompt for downstream LLM")
    lines.append("")
    lines.append("Use only the chunks in this evidence pack. Do not attribute claims to a source unless the claim is supported by that source's chunk. Distinguish explicit evidence, reasonable inference, and limitations. For every concrete claim, include chunk_id or source_ref. If coverage is weak for a vendor or topic, say so.")
    lines.append("")
    lines.append("Suggested answer structure:")
    lines.append("")
    lines.append("1. Short answer")
    lines.append("2. Source-by-source analysis")
    lines.append("3. Explicit evidence")
    lines.append("4. Reasonable inferences")
    lines.append("5. Biases or limits")
    lines.append("6. Convergences and divergences")
    lines.append("7. Operational implications")
    lines.append("")
    return "\n".join(lines)


def as_json(query: str, results: list[tuple[float, dict[str, Any]]]) -> str:
    payload = {
        "query": query,
        "coverage": {
            "vendors": Counter((chunk.get("vendor") or "unknown") for _, chunk in results),
            "topics": Counter((chunk.get("topic") or "unknown") for _, chunk in results),
        },
        "results": [
            {"score": round(score, 4), **chunk}
            for score, chunk in results
        ],
        "llm_guardrail": "Use only the chunks in this evidence pack. Distinguish explicit evidence, reasonable inference, and limitations. Cite chunk_id or source_ref for concrete claims.",
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)


def main() -> int:
    parser = argparse.ArgumentParser(description="Create an evidence pack from repository chunks.")
    parser.add_argument("query", help="Research or comparison query")
    parser.add_argument("--chunks", default=None, help="Path to chunks.jsonl")
    parser.add_argument("--vendor", default=None, help="Optional vendor filter")
    parser.add_argument("--topic", default=None, help="Optional topic filter")
    parser.add_argument("--top-k", type=int, default=12, help="Number of chunks")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    parser.add_argument("--output", default=None, help="Write output to file")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    chunks_path = Path(args.chunks) if args.chunks else root / "data" / "processed" / "chunks.jsonl"
    chunks = filter_chunks(load_chunks(chunks_path), args.vendor, args.topic)
    results = retrieve(args.query, chunks, args.top_k)

    output = as_json(args.query, results) if args.json else as_markdown(args.query, results)

    if args.output:
        out_path = Path(args.output)
        if not out_path.is_absolute():
            out_path = root / out_path
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output, encoding="utf-8")
        print(f"Wrote evidence pack: {out_path}")
    else:
        print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
