@echo off
echo ==========================================================
echo Generating HTML documentation...

if not exist "documentation" mkdir documentation
cd documentation
if not exist "html" mkdir html
cd html
rmdir /s /q SDSPy
del index.html
del SDSPy.html
del search.js
cd ../..

pdoc --output-dir documentation/html/ .\SDSPy\

echo Done !
echo =========================================================