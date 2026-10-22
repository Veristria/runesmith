"""The file-tree benchmark: it counts only the tree it built and stays quick enough for the suite."""

import importlib.util
import json
from pathlib import Path

BENCHMARK = Path(__file__).resolve().parents[1] / "docs" / "benchmarks" / "bench_file_tree.py"


def _benchmark_module():
    spec = importlib.util.spec_from_file_location("bench_file_tree", BENCHMARK)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_benchmark_counts_the_files_it_built_and_skips_the_rest(capsys):
    result = _benchmark_module().main(["--dirs", "3", "--files", "3", "--depth", "3", "--repeat", "1"])

    assert result["files_created"] == 9
    assert result["files_found"] == 9                  # skipped folders and the link target are not counted
    assert result["directories"] == 3
    assert result["skipped_folders"] == [".git", "__pycache__", "node_modules"]
    for name in ("walk_files", "build_environment_map"):
        assert result["timings"][name]["min_s"] >= 0
        assert result["timings"][name]["min_s"] <= result["timings"][name]["median_s"]
        assert result["timings"][name]["median_s"] <= result["timings"][name]["max_s"]
    assert not Path(result["root"]).exists()           # the temporary tree was cleaned up
    out = capsys.readouterr().out
    assert "files found: 9" in out


def test_benchmark_json_output_is_machine_readable(capsys):
    result = _benchmark_module().main(["--dirs", "2", "--files", "2", "--depth", "1", "--repeat", "1", "--json"])

    printed = json.loads(capsys.readouterr().out)
    assert printed["files_found"] == result["files_found"] == 4
    assert set(printed["timings"]) == {"walk_files", "build_environment_map"}
    assert printed["symlink_created"] in (True, False)
