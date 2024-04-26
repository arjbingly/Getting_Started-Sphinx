Sphinx - How to get started?
#############################

How to get started with Sphinx for your Python project.

Why use Sphinx?
****************

Making a documentation website for your python project can be daunting and would tradiationally reauire some web-dev
skills. But Sphinx can be used to generate documentations for your project, it can be used to convert your docstrings
and in code documentation into various output formats like HTML, PDF, LATEX, man-pages, etc.

Pre-requisites
****************

* You have proper documentation for your code. This includes doc strings.
* Make sure that your doc strings follow a standard, eg. PEP, Google, Numpy, etc.
* Highly recommended to use a linter for both your code and docs, like Ruff (my personal favorite).

Tutorial
****************
To tutorial contains some dummy code and documentation, for you to try out sphinx.
* To follow on first clone this repo.
* Go ahead and delete the ``src/docs`` diretory.

1. Install Sphinx
===================

- **for Ubuntu/Debian** : ``sudo apt install python3-sphinx``

*Refer for more details:* `Sphinx Installation <https://www.sphinx-doc.org/en/master/usage/installation.html>`_

1.1 Folder Structure (Recommended)
------------------------------------

I like my docs as a separate folder in ``src``. Therefore, I create a new directory ``docs``.
And many fellow developers seems to use the same convention.

::

      ├── src
      │   ├── docs
      │   ├── package_dir
      │   │   ├── __init__.py
      │   │   ├── module_1.py
      │   │   ├── module_2.py
      │   │   ├── subpackage_dir
      │   │   │   ├── __init__.py
      │   │   │   ├── module_1.py
      │   │   │   ├── module_2.py
      ├── other directories and files not documented
      │   ├── css
      │   │   ├── **/*.css
      │   ├── images
      │   ├── js
      │   ├── index.html
      ├── pyproject.toml
      ├── requirements.txt
      ├── package-lock.json
      └── .gitignore


* Create a ``docs`` directory in ``src``.

2. Quickstart
===================

* Change your location to the previously created `docs` directory.

* Run:

```
sphinx-quickstart
```

This will ask you the following:

1. **Do you wanna separate your build and source?**

   **N**, Since I recommend a folder structure with a separate docs directory.
2. **Name of Project**
3. **Author Name(s)**
4. **Project Release**
5. **Project Language**

If run successfully this will create a `conf.py` file, the make files and folders like `_build`, `_static`,
and `_template`.

3. Extract docs
===================

* Change your location to the `src` directory.
* Run:

```
sphinx-apidoc -o docs package_dir
```
where the ``package_dir`` is ``my_calculator`` for this tutorial.

*Note that: here `-o` flag is the output folder, in our structure this is the `docs` directory, and `package_dir` is*
*the directory with all the code you want to document.*

This will create `.rst` files for each Python module and package.

4. Conf.py changes
===================

The `conf.py` file should be in `docs` folder.  
You can see all the details you specified during the `quickstart` command here.

4.1 OS Syspath Changes
-----------------------

Add the following to the beginning of `conf.py`.

```
import os
import sys
sys.path.insert(0, os.path.abspath(".."))
``` 

*Note that this assumes the above-mentioned folder structure, if you have a different structure, make sure to point it*
*to the source code.*

4.1 Extensions
-----------------------

Sphinx has a lot of useful extensions. These should be added to the ``extensions`` tag. Some of the extensions I use are:

1. ``sphinx.ext.autodoc`` - This extension automatically takes doc strings from your python files.
2. ``sphinx.ext.linkcode`` (Optional) - This extension provides a link to the GitHub code.
   *(Note that this extension requires other configs. Refer to Sphinx extension documentation for more details.)*
3. ``sphinx.ext.viewcode`` (Optional) - This extension is similar to the above extension, instead of linking the code to
   GitHub, it displays the code in a static webpage.
4. ``sphinx.ext.napoleon`` (Optional) - If you write your doc strings using Numpy or Google standard, you need this
   extension.

An example ``extentions`` in the ``conf.py`` file.

::

    extensions = [
        "sphinx.ext.autodoc",
        "sphinx.ext.todo",
        "sphinx.ext.napoleon",
        "sphinx.ext.linkcode",
    ]


4.2 Theme (Optional)
-----------------------

I use a Sphinx theme, which can be installed by running,

``` 
pip install sphinx-rtd-theme 
```

* Change the `html_theme` tag in the `conf.py` to `sphinx_rtd_theme`.

```
html_theme = 'sphinx_rtd_theme'
```

You can find more themes at various sources like `www.sphinx-themes.org/`,
`https://sphinxthemes.com`, etc.

5. Building the docs
======================

To finally generate the docs run the following command from the `docs` directory.

```
make html
```

This will create a `_build` directory, where you can find the html files. Opening the `index.html` shows you the
homepage
of your docs.

*Note that whenever you have any changes to your code or documentation, you just have to run the above command and*
*Sphinx will update your documentation.*

6. Make it better (Optional)
=============================

6.1 Adding other pages
-----------------------

* To add other pages to your sphinx website, you just have to create `.rst` reStructuredText files in the appropriate
  location and add them to your `index.rst` or to the `toctree` of a file already mentioned in `index.rst`.

* For more instructions on defining document structure refer
  `Defining Docuement Structure <https://www.sphinx-doc.org/en/master/usage/quickstart.html#defining-document-structure>`_

* For instructions on how to format reStructuredText refer to
  `reStructuredText Basics <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_

* To follow on this tutorial, copy this ``README.rst`` file to ``src/docs`` and add the following the ``README`` file on
  the toctree. Like shown below

::

>    .. toctree::
>       :maxdepth: 2
>       :caption: Contents:
>
>       mycalculator
>       readme

6.2 Adding examples
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- [https://sphinx-gallery.github.io/stable/index.html]()



References
**********

* [https://www.sphinx-doc.org/en/master/usage/quickstart.html]()
* [https://samnicholls.net/2016/06/15/how-to-sphinx-readthedocs/]()
