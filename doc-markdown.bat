@echo off
echo ==========================================================
echo Generating Markdown documentation...

cd .\SDSPy\
for /D %%i in (*) do (
    echo|set /p="Generatic doc for %%i ... "
    pydoc-markdown -p %%i > ..\documentation\markdown\%%i.md
    echo Done !
)
echo|set /p="Generatic doc for SDSPy ... "
pydoc-markdown -p pySDS > ..\documentation\markdown\SDSPy.md
echo Done !


echo Finished creating Markdown documentation !
echo =========================================================