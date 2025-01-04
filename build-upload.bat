echo ==========================================================
echo Generating Markdown documentation...
echo =========================================================

rem Deleting old dist folder
rmdir /s /q dist/

rem Building...
poetry build

rem This will need an API Key !
twine upload dist/*

