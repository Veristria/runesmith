"""Benchmark Runesmith's file-tree scan (runesmith/envmap.py) on a synthetic tree.

The tree is built in a temporary folder and removed afterwards, so the benchmark writes nothing outside it. It holds
ordinary folders of small Python files, folders the scan must skip (.git, node_modules, __pycache__), and, where the
platform allows one, a symbolic link to a folder outside the tree that must not be followed.

Run it from anywhere with nothing installed beyond Python:

    python docs/benchmarks/bench_file_tree.py
    python docs/benchmarks/bench_file_tree.py --dirs 200 --files 50 --depth 3 --repeat 5
    python docs/benchmarks/bench_file_tree.py --dirs 200 --files 50 --repeat 5 --json
"""

from __future__ import annotations

import argparse
import json
import os
import statistics
import sys
import tempfile
import time
from pathlib import Path
from typing import Any, Callable

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:                      # run from the repository without installing it
    sys.path.insert(0, str(REPO_ROOT))

from runesmith.envmap import build_environment_map, walk_files

SKIP_FOLDERS = (".git", "node_modules", "__pycache__")
FILE_TEXT = "value = 1\n"


def _timed(call: Callable[[], Any], repeat: int) -> dict[str, Any]:
    samples = []
    for _ in range(repeat):
        started = time.perf_counter()
        call()
        samples.append(time.perf_counter() - started)
    return {"min_s": min(samples), "median_s": statistics.median(samples), "max_s": max(samples),
            "samples_s": samples}


def _folder_parts(index: int, depth: int) -> list[str]:
    """Unique leaf folders spread over up to ``depth`` levels: dir_0, level1/dir_1, level1/level2/dir_2, ..."""
    levels = index % depth + 1
    return [f"level{level}" for level in range(1, levels)] + [f"dir_{index}"]


def build_tree(base: Path, *, directories: int, files: int, depth: int) -> dict[str, Any]:
    """Build the synthetic tree under ``base``/tree and return what it holds and could not build."""
    root = base / "tree"
    root.mkdir()
    for index in range(directories):
        folder = root.joinpath(*_folder_parts(index, depth))
        folder.mkdir(parents=True, exist_ok=True)
        for number in range(files):
            (folder / f"file_{number}.py").write_text(FILE_TEXT, encoding="utf-8")
    for name in SKIP_FOLDERS:                            # never counted, at the root and inside a folder
        for folder in (root / name, root / "dir_0" / name):
            folder.mkdir(parents=True, exist_ok=True)
            (folder / "skipped.py").write_text(FILE_TEXT, encoding="utf-8")
    outside = base / "outside"
    outside.mkdir()
    (outside / "outside.py").write_text(FILE_TEXT, encoding="utf-8")
    linked = False
    try:
        os.symlink(outside, root / "link_outside", target_is_directory=True)
        linked = True
    except (OSError, NotImplementedError):
        pass                                             # no privilege for a link: the rest of the tree is enough
    return {"root": root, "files_created": directories * files, "symlink_created": linked}


def run(*, directories: int = 50, files: int = 20, depth: int = 2, repeat: int = 3) -> dict[str, Any]:
    """Build a tree, time the scan and the map on it, then remove the tree. Returns the measurements."""
    with tempfile.TemporaryDirectory(prefix="runesmith-bench-") as temporary:
        built = build_tree(Path(temporary), directories=directories, files=files, depth=depth)
        root: Path = built["root"]
        files_found = len(walk_files(root))
        timings = {
            "walk_files": _timed(lambda: walk_files(root), repeat),
            "build_environment_map": _timed(lambda: build_environment_map(root), repeat),
        }
    return {"directories": directories, "files_per_folder": files, "depth": depth, "repeat": repeat,
            "files_created": built["files_created"], "files_found": files_found,
            "skipped_folders": sorted(SKIP_FOLDERS), "symlink_created": built["symlink_created"],
            "timings": timings, "root": str(root)}


def _milliseconds(seconds: float) -> str:
    return f"{seconds * 1000:.2f} ms"


def main(argv: list[str] | None = None) -> dict[str, Any]:
    parser = argparse.ArgumentParser(description="Benchmark Runesmith's file-tree scan on a synthetic tree.")
    parser.add_argument("--dirs", type=int, default=50, help="number of folders to create (default 50)")
    parser.add_argument("--files", type=int, default=20, help="files per folder (default 20)")
    parser.add_argument("--depth", type=int, default=2, help="deepest folder level (default 2)")
    parser.add_argument("--repeat", type=int, default=3, help="timed runs per function (default 3)")
    parser.add_argument("--json", action="store_true", help="print the measurements as JSON")
    args = parser.parse_args(argv)
    if min(args.dirs, args.files, args.depth, args.repeat) < 1:
        parser.error("--dirs, --files, --depth and --repeat must be at least 1")

    result = run(directories=args.dirs, files=args.files, depth=args.depth, repeat=args.repeat)
    if args.json:
        print(json.dumps(result, indent=2))
        return result
    print(f"file-tree benchmark: {result['directories']} folders x {result['files_per_folder']} files, "
          f"depth {result['depth']}, {result['repeat']} runs, link {result['symlink_created']}")
    print(f"files found: {result['files_found']}")
    for name in ("walk_files", "build_environment_map"):
        timing = result["timings"][name]
        print(f"{name:22} min {_milliseconds(timing['min_s'])}  median {_milliseconds(timing['median_s'])}  "
              f"max {_milliseconds(timing['max_s'])}")
    return result


if __name__ == "__main__":
    main()
