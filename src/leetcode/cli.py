import argparse, importlib, json, pkgutil, sys

def _slug_to_module(slug: str) -> str:
    return slug.replace("-", "_")

def _available_problems():
    import leetcode.problems as problems
    return sorted(m.name for m in pkgutil.iter_modules(problems.__path__) if not m.name.startswith("_"))

def _load_input(as_str, path):
    if as_str and path:
        raise SystemExit("Provide either --input or --input-file.")
    if as_str:
        return json.loads(as_str)
    if path:
        with open(path, "r", encoding="utf-8") as fh:
            return json.load(fh)
    if not sys.stdin.isatty():
        return json.loads(sys.stdin.read())
    return None

def main():
    parser = argparse.ArgumentParser(prog="leetcode", description="Run LeetCode problems with JSON input.")
    sub = parser.add_subparsers(dest="cmd", required=True)
    p_list = sub.add_parser("list", help="List available problems.")
    p_run  = sub.add_parser("run", help="Run a problem.")
    p_run.add_argument("problem")
    p_run.add_argument("--input")
    p_run.add_argument("--input-file")
    args = parser.parse_args()
    if args.cmd == "list":
        print("\n".join(_available_problems()))
        return
    data = _load_input(args.input, args.input_file)
    if data is None:
        raise SystemExit("No input provided. Use --input, --input-file, or pipe JSON.")
    module_name = f"leetcode.problems.{_slug_to_module(args.problem)}"
    mod = importlib.import_module(module_name)
    if not hasattr(mod, "solve"):
        raise SystemExit(f"Module {module_name} has no solve() function.")
    out = mod.solve(**data) if isinstance(data, dict) else mod.solve(data)
    json.dump(out, sys.stdout, ensure_ascii=False)
    sys.stdout.write("\n")
