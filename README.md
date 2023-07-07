# mpl_utils

A collection of helper functions for Matplotlib

## Installation

This package is not distributed on PyPI, it must be installed from source. If using `Poetry` to manage dependencies, installation is:

```bash
poetry add git+https://github.com/colinahill/mpl_utils.git
```

## Dev Setup
This project uses [Poetry](https://python-poetry.org/) to manage dependencies.

### Python environment setup
An environment with Python version `3.11` or later is required. If you don't have this, it can be created using [Pyenv](https://github.com/pyenv/pyenv) which should be installed first. After installing Pyenv, download and install Python `3.11` using

```bash
pyenv install 3.11
```

If you already have Python version `3.11` or later you can skip this step.

### Install
Clone the repo and install the package:

```bash
git clone https://github.com/colinahill/mpl_utils.git && cd mpl_utils
```

(Optional) In the case where Poetry doesn't automatically find the correct Python path, you can set it with

```bash
pyenv local 3.11
poetry env use 3.11
```

Then install the package
```bash
poetry install  # Creates a virtualenv and installs package into it
poetry shell  # Opens a sub-shell in the virtualenv
```

### Development

Install `pre-commit` hooks for code quality:

```bash
pre-commit install
```
