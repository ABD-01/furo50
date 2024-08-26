Customization
=============

Furo50 is a Sphinx extension, not a Sphinx theme. However, it supports several options to customize your documentation's appearance and behavior. For theme-based configuration, please refer to the `Furo theme documentation <https://pradyunsg.me/furo/customisation/>`_.

Sidebar Style 
-------------

CS50's webpage features both crimson and black sidebars for CS50 and CS50X respectively. You can choose which style you prefer:

.. code-block:: python

   furo50_style = "CS50"  # or "CS50X"

- Use ``"CS50"`` for a crimson sidebar (default)
- Use ``"CS50X"`` for a black sidebar

Hide Table of Contents
----------------------

By default, the Furo theme includes a table of contents (TOC) drawer on the right side of the page. You can disable this feature by setting:

.. code-block:: python

   furo50_hide_all_toc = True

.. note::
   While Furo also supports `hiding the contents sidebar <https://pradyunsg.me/furo/customisation/toc/>`_, 
   that option doesn't allow the main content to consume the TOC space on the web page. 
   The Furo50 option provides a more comprehensive hiding solution.

Underline Headings
------------------

If you've spent time on CS50 pages, you might have noticed that all the headings have an underline, which is not the default in Furo. To enable this feature:

.. code-block:: python

   furo50_headings_underline = True

Revert to Original Layout
-------------------------

Furo50 includes several layout changes from the original Furo theme. These changes are detailed in the `design changes <design-changes>`_ page. If you prefer to use the original Furo layout:

.. code-block:: python

   furo50_use_original_layout = True

To see the original layout, you can refer to Furo's webpage or any other documentation that uses the Furo theme.

Applying Customizations
-----------------------

To apply these customizations, add the desired options to your ``conf.py`` file. For example:

.. code-block:: python

   # conf.py
   html_theme = "furo"
   extensions = [
       # ... other extensions ...
       "furo50",
   ]

   # Furo50 customization options
   furo50_style = "CS50"
   furo50_hide_all_toc = False
   furo50_headings_underline = True
   furo50_use_original_layout = False

Remember to rebuild your documentation after making changes to see the effects.