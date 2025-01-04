@echo off
echo ==========================================================
echo Generating Markdown documentation...

if not exist "documentation" mkdir documentation
cd documentation
if not exist "markdown" mkdir markdown
cd ..

cd .\SDSPy\
for /D %%i in (*) do (
    echo|set /p="Generatic doc for %%i ... "
    if not exist "..\documentation\markdown\%%i" mkdir ..\documentation\markdown\%%i
    rem pydoc-markdown -p %%i > ..\documentation\markdown\%%i\%%i.md
    echo Done !
)

cd ../documentation/markdown
rmdir /s /q __pycache__ 
rmdir /s /q trigger
mkdir trigger

cd ../../SDSPy
cd trigger

for %%f in (*.py) do (
    echo|set /p="Generatic doc for %%f ... "
    echo pydoc-markdown -p %%f > ..\..\documentation\markdown\trigger\%%f.md
    echo Done !
)

cd ..

echo|set /p="Generatic doc for SDSPy ... "
pydoc-markdown -p pySDS > ..\documentation\markdown\SDSPy.md
echo Done !




echo Finished creating Markdown documentation !
echo =========================================================