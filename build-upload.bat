@echo off
echo ==========================================================
echo Generating WHL and wheel, and upload them...
echo ==========================================================

rem Deleting old dist folder
if exist "dist" rmdir /s /q dist

rem Building...
poetry build

rem This will need an API Key !
echo ==========================================================
echo Please enter the API Key :
echo ==========================================================
python -m twine upload dist/*

echo ==========================================================
echo Done !
echo ==========================================================

