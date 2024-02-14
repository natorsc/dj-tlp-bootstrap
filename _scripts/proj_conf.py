# -*- coding: utf-8 -*-
"""."""

import shutil
import pathlib
import subprocess
import sys

EXECUTABLE = sys.executable

BASE_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent

ENV_TXT = BASE_DIR.joinpath('env.txt')
ENV = ROOT_DIR.joinpath('.env')


def create_env_file():
    print('[!] Criando arquivo .env [!]')
    shutil.copy2(src=ENV_TXT, dst=ENV)
    print(f'[!] Arquivo .env criado em {ENV} [!]')


def collectstatic():
    subprocess.run(
        args=[EXECUTABLE, 'manage.py', 'collectstatic', '--noinput'],
        cwd=ROOT_DIR,
    )


def makemigrations():
    subprocess.run(
        args=[EXECUTABLE, 'manage.py', 'makemigrations'],
        cwd=ROOT_DIR,
    )


def migrate():
    subprocess.run(
        args=[EXECUTABLE, 'manage.py', 'migrate'],
        cwd=ROOT_DIR,

    )


def create_super_user():
    subprocess.run(
        args=[EXECUTABLE, 'manage.py', 'createsuperuser'],
        cwd=ROOT_DIR,
    )


if __name__ == "__main__":
    create_env_file()
    collectstatic()
    makemigrations()
    migrate()
    # create_super_user()
