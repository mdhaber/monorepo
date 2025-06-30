.. Monorepo documentation master file, created by
   sphinx-quickstart on Sat Jun 28 11:39:56 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Monorepo documentation

This is the public documentation.

Add your content using ``reStructuredText`` syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.


.. toctree::
   :maxdepth: 1
   :caption: Contents:
   
   package1
   package2

We have a tutorial on ``package1``:
   
.. jupyterlite:: ./_static/test.md
   :width: 100%
   :height: 600px
   :prompt: Try JupyterLite!
   :prompt_color: #00aa42
   :new_tab: True
