# Changelog

All notable changes to louis-py are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project adheres
to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

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

- Updated the louis-rs pin from `1b0c7cd7` to `8eecb61e`. No breaking API
  changes; notable upstream changes include a Pike VM regexp
  engine replacing the recursive backtracker, liblouis-compatible
  prepunc/postpunc scanning, UTF-16 surrogate-pair combining in `\x` escapes,
  the `syllable` opcode, and rejection of circular or overly deep table
  inclusion chains.

### Notes

- The Python bitmask -> Rust mode mapping now lives in the bindings
  (`modes_from_bits`), built on louis-rs' public `TranslationModes::{empty, insert}`,
  replacing the `from_bits` helper that previously lived in the louis-rs crate.
- Depends on louis-rs pinned by git revision until a crates.io release exposes the
  required translator option API.
