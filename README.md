# louis-py

Python bindings for [louis](https://github.com/liblouis/louis-rs), a pure-Rust
braille translator.

```python
from louis_py import Translator, Direction

t = Translator(["en-us-g1.ctb"], Direction.FORWARD)
print(t.translate("hello world"))  # ⠓⠑⠇⠇⠕⠀⠺⠕⠗⠇⠙
```

`translate_with_options` additionally reports where every character ended up:

```python
r = t.translate_with_options("Hello", cursor_pos=1)
r.output            # the braille text
r.output_positions  # for each input character, the index of its braille cell
r.input_positions   # for each braille cell, the index of its input character
r.cursor_pos        # index in r.output of the cursor passed in
```

Tables are resolved via `LOUIS_TABLE_PATH`. See `python/louis_py/_louis_py.pyi`
for the full API.
