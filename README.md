<h1 align="center">Furo50</h1>
<p align="center">
  A sphinx extension that turns <a href="https://github.com/pradyunsg/furo">Furo theme</a> into <a href="https://cs50.harvard.edu/college/2019/fall/">CS50</a>'s theme.
</p>

<p align="center">
    <a href="https://github.com/ABD-01/furo50/actions/workflows/tests.yml?branch=master"><img src="https://github.com/ABD-01/furo50/actions/workflows/tests.yml/badge.svg?branch=master" alt="Tests"></a>
    &emsp;
    <a href="https://github.com/ABD-01/furo50/actions/workflows/docs.yml?branch=master"><img src="https://github.com/ABD-01/furo50/actions/workflows/docs.yml/badge.svg?branch=master" alt="Docs"></a>
    &emsp;
    <img src="https://raw.githubusercontent.com/ABD-01/furo50/master/docs/_static/coverage.svg" alt="Coverage">
    &emsp;
    <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black"></a>
    &emsp;
    <a href="https://www.gnu.org/licenses/gpl-3.0"><img src="https://img.shields.io/badge/License-GPLv3-blue.svg" alt="License: GPL v3"></a>
</p>
<p align="center">
    <a href="https://pypi.org/project/furo50/"><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/furo50"></a>
    &emsp;
    <a href="https://pypi.org/project/furo50/"><img alt="PyPI - Pyversions" src="https://img.shields.io/pypi/pyversions/furo50"></a>
</p>

<!-- [![Tests](https://github.com/ABD-01/furo50/actions/workflows/tests.yml/badge.svg?branch=master)](https://github.com/ABD-01/furo50/actions/workflows/tests.yml) &emsp; ![](docs/_static/coverage.svg) &emsp; [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) -->

<!-- [![Documentation](https://github.com/ABD-01/furo50/actions/workflows/docs.yml/badge.svg)](https://github.com/ABD-01/furo50/actions/workflows/docs.yml) -->

<!-- [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) -->


<!-- index.md content start -->

## Prerequisites

To use this extension you will need [Furo][furo link] theme for your project.

Install [furo][furo link]  theme and update html_theme in the [sphinx configuration][conf link]

## Usage

1. Install Furo50 extension in your sphinx environment.
    ```
    pip install furo50
    ```

2. In the [`conf.py`][conf link] configuration file, add [furo50][furo50 link] to the extensions list.
    ```
    extensions = [
        ...
        'furo50'
        ...
    ]
    ```
Your Sphinx documentation’s HTML pages will now be generated with this [CS50][cs50 link] theme! 🎉

## Features
* **CS50-Inspired Design**: Emulates the look and feel of [CS50][cs50 link]'s course pages.
* **Easy Configuration**: Simple configuration addition needed in conf.py for quick setup and customization.
* **Syntax Highlighting**: Incorporates CS50-style syntax highlighting for code blocks, improving code readability.
* **Sidebar Styles**: Offers both <span style="background-color:#a51c30;color:#fff;">crimson (CS50)</span> and <span  style="background-color:#000;color:#fff;">black (CS50X)</span> sidebar options, allowing users to choose their preferred aesthetic.
* **Seamless Furo Integration**: Built on top of the Furo theme, and is compatible with Furo's existing features and customizations.
* and more ...

<!-- index.md content end -->

## Changelog

Visit [furo50/changelog](https://abd-01.github.io/furo50/changelog/)

## Licence
Copyright © 2024, Muhammed Abdullah

This software is made available under the GPL v3.


<!-- Markdown links -->

[furo link]: https://pradyunsg.me/furo/
[furo50 link]: https://github.com/ABD-01/furo50
[cs50 link]: https://cs50.harvard.edu/college/2019/fall/
[conf link]: https://www.sphinx-doc.org/en/master/usage/configuration.html