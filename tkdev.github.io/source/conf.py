# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'tkdev-course'
copyright = '2022, XiangQinxi'
author = 'XiangQinxi'
version = '2.5.2'
release = '2.5.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_copybutton',
    'myst_parser',
    "sphinxcontrib.mermaid",
    'sphinx_markdown_tables',
]

templates_path = ["_templates"]
html_additional_pages = {
    "index": "index.html",
}

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "tkinterDev"
html_theme = "furo"
html_static_path = ['_static']
html_logo = "logo-light-mode.png"
html_theme_options = {
    "navigation_with_keys": True,
}
html_theme_options = {
    "source_repository": "https://github.com/pradyunsg/furo/",
    "source_branch": "main",
    "source_directory": "docs/",
}
# html_static_path = ["_static"]
# html_theme_options = { "light_logo": "logo-light-mode.png", "dark_logo": "logo-dark-mode.png"}
