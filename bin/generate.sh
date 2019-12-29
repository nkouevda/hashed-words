#!/usr/bin/env bash

set -euo pipefail

for func in md5sum sha1sum sha256sum sha512sum; do
  xargs --max-procs 0 -I {} sh -c 'printf "%s %s\n" "$(printf {} | '"$func"' | tr -d "\n -")" {}' \
    < /usr/share/dict/words > "output/words-$func"
done
