
# Furo50 documentation

A sphinx extension that turns [Furo theme][furo link] into [CS50][cs50 link]'s theme.

```{include} ../README.md
:parser: myst_parser.sphinx_
:start-after: <!-- index.md content start -->
:end-before: <!-- index.md content end -->
```

```{toctree}
:hidden:

Home <self>
customisation
```

```{toctree}
:caption: Example
:hidden:

Week 5 Notes <example/week5>
CS50 Docs </cs50docs/index.html#http://>
```

```{toctree}
:caption: Development
:hidden:

kitchen-sink/index
design-changes
changelog
license
```

<!-- Markdown links -->

[furo link]: https://pradyunsg.me/furo/
[furo50 link]: https://github.com/ABD-01/furo50
[cs50 link]: https://cs50.harvard.edu/college/2019/fall/
[conf link]: https://www.sphinx-doc.org/en/master/usage/configuration.html