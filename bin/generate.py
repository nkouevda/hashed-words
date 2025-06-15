#!/usr/bin/env python

import hashlib

name_to_func = {
    "md5sum": hashlib.md5,
    "sha1sum": hashlib.sha1,
    "sha256sum": hashlib.sha256,
    "sha512sum": hashlib.sha512,
}

for name, func in name_to_func.items():
    with open("/usr/share/dict/words", "r") as in_file:
        with open(f"output/words-{name}", "w") as out_file:
            for word in in_file.read().splitlines():
                digest = func(word.encode()).hexdigest()
                out_file.write(f"{digest} {word}\n")
