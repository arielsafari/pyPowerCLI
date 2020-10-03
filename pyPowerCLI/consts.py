import os

_here = os.path.abspath(os.path.dirname(__file__))
_user_home = os.path.expanduser('~')

POWERSHELL_MODULES_DIR = os.path.join(_user_home, r"Documents\WindowsPowerShell\Modules")
POWERSHELL_EXE_PATH = r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
DEFAULT_EXECUTION_POLICY = 'Bypass'

POWERCLI_ZIP_PATH =  os.path.join(_here, r"resources\VMware-PowerCLI.zip")
POWERCLI_MODULE_NAME_REGEX = r'^([A-Za-z\.]+)\/.+$'