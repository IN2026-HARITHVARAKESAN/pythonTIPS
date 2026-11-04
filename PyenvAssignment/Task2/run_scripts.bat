@echo off

echo Running dictionary script with Python 3.6.0
set PYENV_VERSION=3.6.0
call python --version
call python dict_order.py

echo.
echo Running walrus operator script with Python 3.8.0
set PYENV_VERSION=3.8.0
call python --version
call python walrus_operator.py

echo.
echo Both scripts completed.

set PYENV_VERSION=
pause