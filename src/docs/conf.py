# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath(".."))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'calc'
copyright = '2024, bob'
author = 'bob'

# The full version, including alpha/beta/rc tags
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx.ext.autodoc",
              "sphinx.ext.linkcode",  # See linkcode settings below
              "sphinx.ext.napoleon"]

# Napoleon settings
napoleon_google_docstring = True

# Linkcode settings

html_context = {
    "display_github": True,  # Integrate GitHub
    "github_user": "arjbingly",  # Username
    "github_repo": "Getting_Started-Sphinx",  # Repo name
    "github_version": "main",  # Version
    "conf_py_path": "/src/",  # Path in the checkout to the docs root
}


def linkcode_resolve(domain, info):
    if domain != 'py':
        return None
    if not info['module']:
        return None
    filename = info['module'].replace('.', '/')
    # return "https://somesite/sourcerepo/%s.py" % filename
    return f"https://github.com/{html_context['github_user']}/{html_context['github_repo']}/blob/{html_context['github_version']}/{html_context['conf_py_path']}/{filename}.py"


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Sphinx Theme 
# pip install sphinx-rtd-theme
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
