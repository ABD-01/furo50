import pytest
from sphinx.errors import ConfigError


@pytest.mark.sphinx("html", testroot="build")  # using roots/test-build
def test_build(app, status, warning):
    app.build()

    assert app.statuscode == 0
    assert (app.outdir / "index.html").exists()
    assert (app.outdir / "_static/furo50.css").exists(), "CSS file not found in build"
    assert (app.outdir / "_static/marker.js").exists(), "JS file not found in build"


@pytest.mark.xfail(raises=ConfigError)
@pytest.mark.sphinx("html", testroot="build", confoverrides={"html_theme": "not_furo"})
def test_theme_support(app, status, warning):
    app.build()


@pytest.mark.sphinx("html", testroot="build")
def test_config(app, status, warning):
    assert "furo50.css" in [file[0] for file in app.registry.css_files], "CSS file not updated in config"
    assert "marker.js" in [file[0] for file in app.registry.js_files], "JS file not updated in config"

    assert app.config.html_theme_options["light_css_variables"]["color-sidebar-background"] == "#a51c30"
    assert app.config.html_theme_options["dark_css_variables"]["color-sidebar-background"] == "#a51c30"
