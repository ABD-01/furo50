import cssutils
import pytest


@pytest.mark.sphinx("html", testroot="build", confoverrides={"furo50_style": "CS50"})
def test_sidebar_crimson(app, status, warning):
    app.build()
    html = (app.outdir / "index.html").read_text()
    assert "--color-sidebar-background: #a51c30" in html


@pytest.mark.sphinx("html", testroot="build", confoverrides={"furo50_style": "CS50x"})
def test_sidebar_black(app, status, warning):
    app.build()
    html = (app.outdir / "index.html").read_text()
    assert "--color-sidebar-background: #000" in html


@pytest.mark.sphinx("html", testroot="build", confoverrides={"furo50_hide_all_toc": True})
def test_hide_toc(app, status, warning):
    app.build()
    css_file = app.outdir / "_static" / "furo50.css"
    assert css_file.exists()
    css_text = css_file.read_text()
    parser = cssutils.CSSParser()
    stylesheet = parser.parseString(css_text)
    toc_display = "block"
    for rule in stylesheet:
        if rule.type == rule.STYLE_RULE and ".toc-drawer" in rule.selectorText:
            toc_display = rule.style.getPropertyValue("display")
    assert toc_display == "none", "Toc should be hidden"
