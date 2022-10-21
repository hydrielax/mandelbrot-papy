# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys, os 
sys.path.insert(0,os.path.abspath("../.."))

project = 'mandelbrot-papy'
copyright = '2022, Alexis Delage et Paul Trincklin'
author = 'Alexis Delage et Paul Trincklin'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.napoleon', # interprete les formats de docstring de google et numpy (en plus de .rst)
              'sphinx.ext.viewcode', # Donne accés au code source depuis la doc
              'myst_parser'] 
source_suffix=[".rst", ".md"]

templates_path = ['_templates']
exclude_patterns = []

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'bizstyle'
html_static_path = ['_static']