#!/bin/bash
if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <input_dir> <output_dir> [--max_depth N]"
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "$SCRIPT_DIR/collect_files.py" "$@"