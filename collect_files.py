import argparse, os, shutil
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument("input_dir", type=Path)
p.add_argument("output_dir", type=Path)
p.add_argument("--max_depth", type=int)
args = p.parse_args()

src, dst = args.input_dir, args.output_dir
dst.mkdir(parents=True, exist_ok=True)
counts = {}

for root, dirs, files in os.walk(src):
    rootp = Path(root)
    for fn in files:
        fp = rootp / fn
        rel = fp.relative_to(src).parts
        dirs_only, name = rel[:-1], rel[-1]

        if args.max_depth is None:
            target_subdirs = ()
        else:
            if len(dirs_only) <= args.max_depth:
                target_subdirs = tuple(dirs_only)
            else:
                target_subdirs = (dirs_only[-1],)

        outdir = dst.joinpath(*target_subdirs)
        outdir.mkdir(parents=True, exist_ok=True)

        dest = outdir / name
        if dest.exists():
            stem, suf = os.path.splitext(name)
            counts[name] = counts.get(name, 1) + 1
            name = f"{stem}({counts[name]}){suf}"
            dest = outdir / name
        else:
            counts[name] = 1

        shutil.copy(fp, dest)
