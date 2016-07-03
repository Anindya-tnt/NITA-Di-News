from cx_Freeze import setup, Executable
import sys
import os


base= None

if sys.platform == 'win32':
    ba = "Win32GUI"


execu = [Executable(script = "nita_di_news.py",shortcutName="nita_di_news",
            shortcutDir="DesktopFolder", base = ba, copyDependentFiles=True,
    appendScriptToExe=True,
    appendScriptToLibrary=False, targetName = "nita_di_news.exe")]


    
setup(
    name="NITA NEWS",
    options = {"build_exe": {"packages":["os"],"include_files":["..////Resources//nita_icon.ico"]}},
    version = "1.1",
    description = "View Latest News currently at NITA website",
    executables = execu)
