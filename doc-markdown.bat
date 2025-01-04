@echo off
echo ==========================================================
echo Generating Markdown documentation...
echo =========================================================

if not exist "documentation" mkdir documentation
cd documentation
if not exist "markdown" mkdir markdown
cd ..

cd .\SDSPy\
for /D %%i in (*) do (
    echo|set /p="Generatic doc for %%i ... "
    if not exist "..\documentation\markdown\%%i" mkdir ..\documentation\markdown\%%i
    pydoc-markdown -p %%i > ..\documentation\markdown\%%i\%%i.md
    echo Done !
)

cd ../documentation/markdown
rmdir /s /q __pycache__ 
rmdir /s /q trigger
mkdir trigger

cd ../../SDSPy/trigger

for %%f in (*.py) do (
    echo|set /p="Generatic doc for %%~nf ... "
    pydoc-markdown -p %%~nf > ..\..\documentation\markdown\trigger\%%~nf.md
    echo Done !
)

cd ../..
cd documentation/markdown/trigger
if exist "__init__.md" del __init__.md
cd ../../../SDSPy

for %%f in (*) do echo %%f

echo|set /p="Generatic doc for SDSPy ... "
pydoc-markdown -p pySDS > ..\documentation\markdown\SDSPy.md
echo Done !

echo =========================================================
echo Finished creating Markdown documentation !
echo =========================================================

pause