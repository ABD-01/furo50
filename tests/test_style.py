import pytest
import cssutils


def read_text(path):
    """
    Support function to give backward compatibility with older sphinx (v2).
    """
    if hasattr(path, "read_text"):
        return path.read_text()
    return path.text()


@pytest.mark.sphinx("html", testroot="build", confoverrides={"furo50_style": "CS50"})
def test_sidebar_crimson(app, status, warning):
    app.build()
    html = read_text(app.outdir / "index.html")
    assert "--color-sidebar-background: #a51c30" in html


@pytest.mark.sphinx("html", testroot="build", confoverrides={"furo50_style": "CS50x"})
def test_sidebar_black(app, status, warning):
    app.build()
    html = read_text(app.outdir / "index.html")
    assert "--color-sidebar-background: #000" in html


@pytest.mark.sphinx("html", testroot="build", confoverrides={"furo50_hide_all_toc": True})
def test_hide_toc(app, status, warning):
    app.build()
    css_file = app.outdir / "_static" / "furo50.css"
    assert css_file.exists()
    css_text = read_text(css_file)
    parser = cssutils.CSSParser()
    stylesheet = parser.parseString(css_text)
    toc_display = "block"
    for rule in stylesheet:
        if rule.type == rule.STYLE_RULE and ".toc-drawer" in rule.selectorText:
            toc_display = rule.style.getPropertyValue("display")
    assert toc_display == "none", "Toc should be hidden"
