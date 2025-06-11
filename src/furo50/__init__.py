"""Sphinx Extension that turns furo theme into CS50's theme."""

__version__ = "1.0.0b2"

import re
from pathlib import Path
from typing import Any, Callable, Dict

from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.errors import ConfigError

# from bootstarp
# fmt: off
white       = '#fff'
gray_100    = '#f8f9fa'
gray_200    = '#e9ecef'
gray_300    = '#dee2e6'
gray_400    = '#ced4da'
gray_500    = '#adb5bd'
gray_600    = '#6c757d'
gray_700    = '#495057'
gray_800    = '#343a40'
gray_900    = '#212529'
black       = '#000'
# fmt: on

hex2rgb: Callable[[str], str] = lambda h: "{},{},{}".format(*(int(h[i : i + 2], 16) for i in (1, 3, 5)))

link_color = "#a51c30"
link_color_dark = "#ef9aa4"

body_color = gray_900
body_secondary_color = f"rgba({hex2rgb(body_color)},.75)"  # rgba($body-color, .75)
body_tertiary_color = f"rgba({hex2rgb(body_color)},.5)"  # rgba($body-color, .5)
border_color = gray_300  # "#dee2e6"

body_bg = white  # "#fff"
body_secondary_bg = gray_200  # "#e9ecef"
nav_link_hover_color = f"color-mix(in srgb, white 70%, {link_color})"

body_color_dark = gray_300  # "#dee2e6"
body_secondary_color_dark = f"rgba({hex2rgb(body_color_dark)},.75)"
body_tertiary_color_dark = f"rgba({hex2rgb(body_color_dark)},.5)"
border_color_dark = gray_700  # "#495057"

body_bg_dark = gray_900  # "#212529"
body_secondary_bg_dark = gray_800  # "#343a40"
nav_link_hover_color_dark = f"color-mix(in srgb, black 70%, {link_color_dark})"

# fmt: off
html_theme_options = {
    "light_css_variables": {
        "link-color": f"{link_color}",

        "color-foreground-primary": f"{body_color}",
        "color-foreground-secondary": f"{body_secondary_color}",
        "color-foreground-muted": f"{body_tertiary_color}",
        "color-foreground-border": f"{border_color}",

        "color-background-primary": f"{body_bg}",
        "color-background-secondary": f"{body_secondary_bg}",
        "color-background-hover": f"{nav_link_hover_color}",
        "color-background-border": f"{border_color}",
        
        "color-brand-primary": f"{link_color}",
        "color-brand-content": f"{link_color}",
        "color-brand-visited": f"{link_color}",
    },
    "dark_css_variables": {
        "link-color-dark": f"{link_color_dark}",

        "color-foreground-primary": f"{body_color_dark}",
        "color-foreground-secondary": f"{body_secondary_color_dark}",
        "color-foreground-muted": f"{body_tertiary_color_dark}",
        "color-foreground-border": f"{border_color_dark}",

        "color-background-primary": f"{body_bg_dark}",
        "color-background-secondary": f"{body_secondary_bg_dark}",
        "color-background-hover": f"{nav_link_hover_color_dark}",
        "color-background-border": f"{border_color_dark}",

        "color-brand-primary": f"{link_color_dark}",
        "color-brand-content": f"{link_color_dark}",
        "color-brand-visited": f"{link_color_dark}",

        "color-card-marginals-background": "var(--color-background-secondary)",  # for the dropdown card color

        "color-sidebar-background": f"{link_color}",
    },
}
# fmt: on

sidebar_theme_options = {
    "color-sidebar-background": link_color,
    "color-sidebar-background-border": "transparent",
    "color-sidebar-brand-text": white,
    "color-sidebar-caption-text": "rgba(255, 255, 255, 0.5)",
    "color-sidebar-search-foreground": gray_200,
    "color-sidebar-search-border": gray_300,
    "color-sidebar-item-background--hover": "var(--color-sidebar-item-background)",
}

header_theme_options = {
    "color-header-background": link_color,
    "color-header-text": white,
}

html_theme_options["light_css_variables"].update(**sidebar_theme_options, **header_theme_options)
html_theme_options["dark_css_variables"].update(**sidebar_theme_options, **header_theme_options)

pygments_style = "igor"
pygments_dark_style = "github-dark"

CRIMSON_BG = 0
BLACK_BG = 1


def trim_css(text_css: str) -> str:
    text_css = re.sub(r"/\*.*?\*/", "", text_css, flags=re.DOTALL)  # Remove comments
    text_css = re.sub(r"^\s+|\s+$", "", text_css, flags=re.MULTILINE)  # Remove leading/trailing whitespace on each line
    text_css = re.sub(r"\s{2,}", " ", text_css)  # Collapse multiple whitespace characters into a single space
    text_css = re.sub(r"\s*([\{\}\:\;\,])\s*", r"\1", text_css)  # Remove whitespace around special characters
    return text_css


def update_theme_options(options: Dict[str, Any], sidebar_bg: int = CRIMSON_BG) -> None:
    options["light_css_variables"] = options.get("light_css_variables", {})
    options["dark_css_variables"] = options.get("dark_css_variables", {})

    options["light_css_variables"].update(html_theme_options["light_css_variables"])
    options["dark_css_variables"].update(html_theme_options["dark_css_variables"])

    if sidebar_bg == BLACK_BG:
        options["light_css_variables"]["color-sidebar-background"] = black
        options["dark_css_variables"]["color-sidebar-background"] = black
        options["light_css_variables"]["color-header-background"] = black
        options["dark_css_variables"]["color-header-background"] = black


def update_css_files(app: Sphinx) -> None:
    static_path = (Path(app.outdir) / "_static").absolute()
    static_path.mkdir(exist_ok=True)
    app.config.html_static_path.append(str(static_path))
    css_path = static_path / "furo50.css"

    styles_path = Path(__file__).parent / "_static" / "css"
    content = (styles_path / "cs50.css").read_text()
    content += (styles_path / "sidebar-scroll.css").read_text()

    if not app.config.furo50_use_original_layout:
        content += (styles_path / "furo50_scaffold.css").read_text()

    if app.config.furo50_hide_all_toc:
        content += (styles_path / "hide-all-toc.css").read_text()

    if app.config.furo50_headings_underline:
        content += (styles_path / "headings-underline.css").read_text()

    css_path.write_text(trim_css(content))
    app.add_css_file(css_path.name, ref="stylesheet")


def add_marker_styling(app: Sphinx) -> None:
    app.add_js_file(
        "https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js",
        integrity="sha512-v2CJ7UaYy4JwqLDIrZUI/4hqeoQieOmAZNXBeQyjo21dadnwR+8ZaIJVT8EE2iyI61OV8e6M8PP2/4hpQINQ/g==",
        crossorigin="anonymous",
        referrerpolicy="no-referrer",
    )
    app.config.html_static_path.append(str(Path(__file__).parent / "_static" / "js"))
    app.add_js_file("marker.js")


def update_font_config(app: Sphinx) -> None:
    # PT Sans Font
    app.add_css_file(
        "https://fonts.googleapis.com/css?family=PT+Sans%7CPT+Sans:bold%7CPT+Sans:ital",
        ref="stylesheet",
    )
    app.add_js_file("https://ajax.googleapis.com/ajax/libs/webfont/1.6.26/webfont.js", priority=800)
    app.add_js_file(
        None,
        body="WebFont.load({google: {families: ['PT Sans', 'PT Sans:bold', 'PT Sans:ital']}});",
        priority=801,
    )
    # Font Awesome
    app.add_css_file(
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css",
        rel="stylesheet",
        integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==",
        crossorigin="anonymous",
        referrerpolicy="no-referrer",
    )


def _update_theme_options(app: Sphinx, config: Config) -> None:
    if app.config.html_theme != "furo":
        raise ConfigError(
            "Furo50 only supports furo theme." "Either change your theme or remove furo50 from the extensions list."
        )
    furo50_style = config.furo50_style.upper()
    if furo50_style not in ["CS50", "CS50X"]:
        raise ConfigError(f"Unknown furo50_style: {furo50_style}.\nMust be one of (CS50, CS50x)")
    options = app.config.html_theme_options
    update_theme_options(options, sidebar_bg=BLACK_BG if furo50_style == "CS50X" else CRIMSON_BG)
    app.config.pygments_style = pygments_style
    app.config.pygments_dark_style = pygments_dark_style


def _builder_inited(app: Sphinx) -> None:
    update_css_files(app)
    update_font_config(app)
    add_marker_styling(app)


def setup(app: Sphinx) -> Dict[str, Any]:
    app.add_config_value("furo50_style", default="CS50", rebuild="env", types=[str])
    app.add_config_value("furo50_hide_all_toc", default=False, rebuild="env", types=[bool])
    app.add_config_value("furo50_headings_underline", default=False, rebuild="env", types=[bool])
    app.add_config_value("furo50_use_original_layout", default=False, rebuild="env", types=[bool])
    app.connect("config-inited", _update_theme_options, priority=1000)
    app.connect("builder-inited", _builder_inited)
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
        "version": __version__,
    }
