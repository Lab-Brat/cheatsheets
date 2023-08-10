### Combined Commands and One-Liners

* `for f in *_prefix_*.epub; do mv "$f" "${f/_prefix_}"; done` -> remove `_prefix_` from all filenames

