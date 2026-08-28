def test_translate_with_options_output():
    from louis_py import Translator

    t = Translator(["mini.ctb"])
    r = t.translate_with_options("abc")
    assert r.output == "⠁⠃⠉"


def test_emphasis_not_populated_today():
    # Encodes the remaining upstream limitation: the pipeline reports no
    # emphasis spans. Flip this when it starts filling them.
    from louis_py import Translator

    t = Translator(["mini.ctb"])
    r = t.translate_with_options("abc")
    assert r.emphasis is None


def test_repr():
    from louis_py import Translator

    t = Translator(["mini.ctb"])
    r = t.translate_with_options("a")
    assert "TranslationResult" in repr(r)
