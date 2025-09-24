import argparse
import importlib
import json
import pkgutil
import sys


def _slug_to_module(slug: str) -> str:
    return slug.replace("-", "_")


def _available_problems() -> list[str]:
    import leetcode.problems as problems

    return sorted(
        m.name for m in pkgutil.iter_modules(problems.__path__) if not m.name.startswith("_")
    )


def _load_input(as_str: str | None, path: str | None):
    if as_str and path:
        raise SystemExit("Provide either --input or --input-file.")
    if as_str:
        return json.loads(as_str)
    if path:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    if not sys.stdin.isatty():
        return json.loads(sys.stdin.read())
    return None


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="leetcode",
        description="Run LeetCode problems with JSON input.",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    # list
    p_list = sub.add_parser("list", help="List available problems.")
    p_list.set_defaults(list_cmd=True)

    # run
    p_run = sub.add_parser("run", help="Run a problem.")
    p_run.add_argument("problem", help="Problem slug (e.g., two-sum or two_sum).")
    p_run.add_argument("--input", help="JSON input string.", default=None)
    p_run.add_argument("--input-file", help="Path to JSON input file.", default=None)

    args = parser.parse_args()

    if getattr(args, "list_cmd", False):
        print("\n".join(_available_problems()))
        return

    data = _load_input(args.input, args.input_file)
    if data is None:
        raise SystemExit("No input provided. Use --input JSON, --input-file FILE, or pipe JSON.")

    module_name = f"leetcode.problems.{_slug_to_module(args.problem)}"
    try:
        mod = importlib.import_module(module_name)
    except ModuleNotFoundError as e:
        raise SystemExit(
            f"Problem '{args.problem}' not found. " f"Available: {', '.join(_available_problems())}"
        ) from e

    if not hasattr(mod, "solve"):
        raise SystemExit(f"Module '{module_name}' has no solve(...) function.")

    if isinstance(data, dict):
        out = mod.solve(**data)
    elif isinstance(data, list):
        out = mod.solve(*data)
    else:
        out = mod.solve(data)

    json.dump(out, sys.stdout, ensure_ascii=False)
    sys.stdout.write("\n")
