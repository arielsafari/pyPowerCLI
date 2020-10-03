from re import match
from zipfile import ZipFile
import os
import shutil

from . import consts
from .powershell import Powershell


def install_powercli():
    """ Install PowerCLI modules for the current user. """
    if is_installed():
        return
    
    powercli_zip = ZipFile(consts.POWERCLI_ZIP_PATH)

    modules_dir = Powershell.get_modules_dir(should_create=True)
    powercli_zip.extractall(path=modules_dir)


def uninstall_powercli():
    """ Uninstalls all PowerCLI modules from the current user. """
    powercli_modules_names = __get_powercli_modules_names(ZipFile(consts.POWERCLI_ZIP_PATH))
    modules_dir = Powershell.get_modules_dir()
    
    for module in os.listdir(modules_dir):
        if module in powercli_modules_names:
            shutil.rmtree(os.path.join(modules_dir, module))


def is_installed():
    """ Checks if all PowerCLI modules are installed correctly. """
    modules_dir = Powershell.get_modules_dir()

    if not os.path.exists(modules_dir):
        return False

    modules_in_powershell_dir = os.listdir(modules_dir)

    for module in __get_powercli_modules_names(ZipFile(consts.POWERCLI_ZIP_PATH)):
        if module not in modules_in_powershell_dir:
            return False
    
    return True


def __get_powercli_modules_names(powercli_zip):
    """ Extracts from the PowerCLI zip the PowerCLI modules names. """
    if not isinstance(powercli_zip, ZipFile):
        raise TypeError("The argument 'powercli_zip' isn't of type 'ZipFile'.")

    modules_names = []
    for single_file in powercli_zip.namelist():
        module_match = match(consts.POWERCLI_MODULE_NAME_REGEX, single_file)
        
        if not module_match:
            continue
        
        module_name = module_match.groups()[0]
        if module_name not in modules_names:
            modules_names.append(module_name)
    
    return modules_names
