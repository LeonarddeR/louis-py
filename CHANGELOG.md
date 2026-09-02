# Changelog

All notable changes to louis-py are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project adheres
to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `search_path=` keyword on `Translator`: the directories, in order, in which
  table names and their `include` lines are looked up. `None` (the default)
  keeps reading `LOUIS_TABLE_PATH`. A host that manages its own table
  directories passes them here instead of mutating the environment variable
  around every constructor call. Nothing beyond the given list is searched: a
  table's own directory only when listed, and an absolute table name resolves
  against any non-empty search path.
- Position mapping on `TranslationResult`. The `output_positions`,
  `input_positions` and `cursor_pos` fields used to always be `None`;
  `Translator.translate_with_options` now fills them in.
  `output_positions[i]` is the index of the braille cell that the input
  character at index `i` translated to, and `input_positions[j]` is the
  index of the input character that the braille cell at index `j` came
  from. Both count characters, so they index the input and output strings
  directly. `cursor_pos` holds the translated position of the cursor
  passed as `cursor_pos=`, and stays `None` when none is passed; a cursor
  past the end of the input maps past the end of the output.
- `Translator.from_table_source(table, direction=Direction.FORWARD)`: build a
  translator from raw table source text held in memory. Does not resolve
  `include` directives; table text containing one raises `TableParseError`.
- Initial release of `louis-py`, PyO3 bindings for the
  [louis-rs](https://github.com/liblouis/louis-rs) braille translator, extracted
  into its own repository.
  - `Translator` with GIL-released `translate` / `translate_with_options`.
  - `Direction` enum and `TranslationMode` flags (`enum.IntFlag`).
  - `TranslationResult` and `EmphasisSpan` result types.
  - Exception hierarchy: `LouisError`, `TableParseError`, `TranslationError`.
  - Type stubs (`_louis_py.pyi`) and `py.typed` marker.
  - Built with maturin, `abi3-py311` (single wheel for Python 3.11+).

### Changed

- Updated the louis-rs pin from `1b0c7cd7` to `048deaba`. No breaking API
  changes; notable upstream changes include position and cursor mapping over
  the whole translation pipeline, a Pike VM regexp engine replacing the
  recursive backtracker, liblouis-compatible prepunc/postpunc scanning,
  UTF-16 surrogate-pair combining in `\x` escapes, the `syllable` opcode,
  caps-passage (`begcaps`/`begcapsphrase`) indication, and rejection of
  circular or overly deep table inclusion chains.
- Updated the louis-rs pin from `048deaba` to `98208e28`. Notable upstream
  changes: a caller-supplied table search path (`Translator::with_search_path`,
  exposed here as `search_path=`); competing translation rules ranked by the
  number of characters they consume before their `before`/`after` conditions;
  case-sensitive `comp6` lookup; an `include`d `.dic` hyphenation dictionary
  embedded while includes are expanded, with bad dictionaries reported as table
  errors naming the file; table read errors naming the file and the I/O error.
  The never-populated `TranslationResult::spacing` was removed upstream;
  louis-py never exposed it.

### Notes

- The Python bitmask -> Rust mode mapping now lives in the bindings
  (`modes_from_bits`), built on louis-rs' public `TranslationModes::{empty, insert}`,
  replacing the `from_bits` helper that previously lived in the louis-rs crate.
- Depends on louis-rs pinned by git revision until a crates.io release exposes the
  required translator option API.
