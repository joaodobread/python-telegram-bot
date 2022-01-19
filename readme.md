# TelegramBot

## Instalation

> Prerequisites:

-   python ^3.10
-   python3-pip

## Configuring the dev environment

```shell
$ pip install poetry

$ poetry shell

(telebot-05jPPhOV-py3.10)$ poetry install

(telebot-05jPPhOV-py3.10)$ commit-linter
```

## Poetry

[Poetry](https://python-poetry.org/docs/) is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

## Commits

> All commits are using the [conventional-commits](https://www.conventionalcommits.org/en/v1.0.0/)

A specification for adding human and machine readable meaning to commit messages.

<!--
```shell
``` -->

## MongoDB

Simple repository example

```python
from src.database.base_repository import Repository


class User(Repository):
    def __init__(self):
        super().__init__("database", "collection")

```
