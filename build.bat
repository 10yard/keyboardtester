venv\Scripts\pyinstaller --onefile keytest.py --clean --windowed --icon resources\kade.ico

xcopy resources dist\resources /S /i /Y
copy version.txt dist\ /Y
copy license.txt dist\ /Y
copy readme.md  dist\ /Y
