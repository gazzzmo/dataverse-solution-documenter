"""
Command line interface for Dataverse Solution Documenter (dsd).
"""
import argparse
import sys
from pathlib import Path

from app.core import process_solution_zip


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="dsd",
        description="Dataverse Solution Documenter — Generate structured Markdown documentation from Dataverse solution .zip archives.",
    )
    parser.add_argument(
        "-i",
        "--input",
        dest="input_file",
        required=True,
        type=Path,
        help="Path to the Dataverse solution .zip file.",
    )
    parser.add_argument(
        "-o",
        "--output",
        dest="output_dir",
        required=True,
        type=Path,
        help="Directory where generated Markdown documentation files will be written.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose output logging.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = create_parser()
    args = parser.parse_args(argv)

    input_path = args.input_file.resolve()
    output_path = args.output_dir.resolve()

    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}", file=sys.stderr)
        return 1

    if not input_path.is_file() or input_path.suffix.lower() != ".zip":
        print(f"Error: Input file must be a .zip archive: {input_path}", file=sys.stderr)
        return 1

    try:
        if args.verbose:
            print(f"Processing solution: {input_path}")
        
        parsed, docs = process_solution_zip(input_path)
        
        solution_name = parsed.get("solution", {}).get("display_name") or parsed.get("solution", {}).get("unique_name") or input_path.stem
        if args.verbose:
            print(f"Solution: {solution_name} ({len(docs)} document(s) generated)")

        output_path.mkdir(parents=True, exist_ok=True)

        for filename, content in docs.items():
            doc_file = output_path / filename
            doc_file.write_text(content, encoding="utf-8")
            if args.verbose:
                print(f"  ✓ Written: {filename} ({len(content):,} chars)")

        print(f"Successfully generated {len(docs)} documentation file(s) in: {output_path}")
        return 0

    except Exception as e:
        print(f"Error processing solution: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
