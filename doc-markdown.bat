@echo off
echo ==========================================================
echo Generating Markdown documentation...
echo ==========================================================

rem Creating folder structure
if not exist "documentation" mkdir documentation
cd documentation
if not exist "markdown" mkdir markdown
cd ..

rem Iterating over first level folder to generate docs.
rem This is fine for simple modules
cd .\SDSPy\
for /D %%i in (*) do (
    echo|set /p="Generatic doc for %%i ... "
    if not exist "..\documentation\markdown\%%i" mkdir ..\documentation\markdown\%%i
    pydoc-markdown -p %%i > ..\documentation\markdown\%%i\%%i.md
    echo Done !
)

rem Since trigger is too complex, we create multiples files in it.
rem First, delete previously generated file (and useless files btw) and create an empty folder
cd ../documentation/markdown
rmdir /s /q __pycache__ 
rmdir /s /q trigger
mkdir trigger

rem Naviguate to the trigger folder
cd ../../SDSPy/trigger

rem Generate a doc per file
for %%f in (*.py) do (
    echo|set /p="Generatic doc for %%~nf ... "
    pydoc-markdown -p %%~nf > ..\..\documentation\markdown\trigger\%%~nf.md
    echo Done !
)


rem Deleting some artifacts files
cd ../..
cd documentation/markdown/trigger
if exist "__init__.md" del __init__.md
cd ../../../SDSPy

rem Generatic global doc project
echo|set /p="Generatic doc for SDSPy ... "
pydoc-markdown -p pySDS > ..\documentation\markdown\SDSPy.md
echo Done !

echo =========================================================
echo Finished creating Markdown documentation !
echo =========================================================

pause