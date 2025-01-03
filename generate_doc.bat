echo ======================================================================
echo Let's generate all of the documentation for the project !
echo ======================================================================

cd SDSPy
for /d %%D in (*) do (
    dir /b /a-d
)
cd ..

# pydoc-markdown -p . --render-toc >.\{file[:-3]+".md"}