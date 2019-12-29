# hashed-words

Each `output/words-*`, e.g. [`output/words-md5sum`](output/words-md5sum),
contains hashes of all words in `/usr/share/dict/words`.

## Generation

The naive shell approach [`bin/generate.sh`](bin/generate.sh) incurs a
tremendous amount of overhead, since each hash is a separate process. Even with
parallelization via `xargs`, it takes about 35 minutes, which is roughly 450
hashes per second.

[`bin/generate.py`](bin/generate.py) is significantly faster, despite being
single threaded: it takes about 1.5 seconds, or roughly 625k hashes per second.
