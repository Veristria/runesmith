# Benchmarks

`bench_file_tree.py` measures the file-tree scan that Runesmith does before it maps a folder: `walk_files` and
`build_environment_map(workspace)` without `probe`, both from `runesmith/envmap.py`. It builds a synthetic tree in a
temporary folder, includes folders the scan must skip (`.git`, `node_modules`, `__pycache__`) and, where the platform
allows one, a symbolic link it must not follow, times a few runs with `time.perf_counter`, prints the minimum, median
and maximum for each function, and removes the tree afterwards.

The script uses only the Python standard library (Python 3.11 or newer). Run it from the repository:

```bash
python docs/benchmarks/bench_file_tree.py
python docs/benchmarks/bench_file_tree.py --dirs 200 --files 50 --depth 3 --repeat 5
python docs/benchmarks/bench_file_tree.py --dirs 200 --files 50 --depth 3 --repeat 5 --json
```

`--dirs` is the number of folders, `--files` the files in each folder and `--depth` the deepest folder level. The
output names the number of files found and the timings, for example on one Windows machine:

```
file-tree benchmark: 200 folders x 50 files, depth 3, 5 runs, link True
files found: 10000
walk_files             min 55.48 ms  median 57.48 ms  max 59.13 ms
build_environment_map  min 534.00 ms  median 538.02 ms  max 586.81 ms
```

`--json` prints the same measurements as an object with `files_found`, `files_created`, `directories`,
`files_per_folder`, `depth`, `repeat`, `symlink_created` and `timings` (each with `min_s`, `median_s`, `max_s` and
every sample). The numbers are only comparable on the same machine and file system; run it before and after a change
to the scan to see whether the change made it slower.

The smoke test `tests/test_bench_file_tree.py` runs the same `main()` on a tiny tree and checks the counts and the
cleanup, so the suite stays fast:

```bash
python -m pytest tests/test_bench_file_tree.py
```
