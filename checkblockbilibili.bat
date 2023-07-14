wmic process where caption="python.exe" get commandline /value | findstr "testdetectwnd.py"
if ERRORLEVEL 1 blockbilibilipy.bat