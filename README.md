# Python base project with the following:

[![Poetry](https://img.shields.io/badge/poetry-blue?logo=poetry)](https://github.com/python-poetry/poetry)

[![pre-commit](https://img.shields.io/badge/pre%20commit-orange?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Gitlint](https://img.shields.io/badge/gitlint-yellow?logo=git)](https://github.com/jorisroovers/gitlint)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Linting pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
[![Flake8](https://img.shields.io/badge/flake8-green?logo=python)](https://github.com/pylint-dev/pylint)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

[![Pytest](https://img.shields.io/badge/pytest-red?logo=pytest)](https://github.com/pytest-dev/pytest)

### Setting up project

#### 1. Install poetry

```
curl -sSL https://install.python-poetry.org | python3 -
```

#### 2. Install dependency

```
 poetry install --without dev, test
```

#### 3. Install pre-commit

```
pre-commit install
pre-commit install --hook-type commit-msg
```

#### 4. Add list emails of contributor to AUTHORS.md

```
1. abc@gmail.com
2. def@gmail.com
3. ...
```
