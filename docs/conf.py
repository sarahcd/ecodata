# Projects sharing this configuration file
multiproject_projects = {
    "package": {},
    "apps": {}
}

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "multiproject",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",  # Create neat summary tables for modules/classes/methods etc
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    'myst_nb',
]

pygments_style='default'

# Use saved output in notebooks rather than executing on build
# Since the examples use large datasets not in the git repo, they need to execute locally
jupyter_execute_notebooks = "off"

autosummary_generate = True  # Turn on sphinx.ext.autosummary
add_module_names = False

source_suffix = {
    '.rst': 'restructuredtext',
    '.ipynb': 'myst-nb',
    '.md': 'myst-nb',
    '.myst': 'myst-nb',
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

todo_include_todos = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = 'pydata_sphinx_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

html_theme_options = {
    "github_url": "https://github.com/jemissik/pymovebank",
    #   "show_nav_level": 4,

}