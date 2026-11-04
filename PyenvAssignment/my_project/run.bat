@echo off

echo Activating virtual environment...
call my_env\Scripts\activate.bat

echo.
echo Checking Python version...
python --version

echo.
echo Running test.py...
python test.py

echo.
pause