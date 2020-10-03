import os
import subprocess

from . import consts


class Powershell(object):
    """
    Represents all the methods related to Powershell.
    """
    
    @staticmethod
    def get_modules_dir(should_create=False):
        """ Returns the 'modules' directory of Powershell. """

        if should_create and not os.path.exists(consts.POWERSHELL_MODULES_DIR):
            os.makedirs(consts.POWERSHELL_MODULES_DIR)
    
        return consts.POWERSHELL_MODULES_DIR

    @staticmethod
    def execute_command(command):
        """
        Executes a Powershell one-liner command.
        Returns - return code.
        If an exception in Powershell is thrown, the function throws PowershellException.
        """
        return Powershell.__run_powershell('-Command {}'.format(command))

    @staticmethod
    def execute_file(file_path, arguments=''):
        """
        Executes a Powershell script file (ps1) with given arguments.
        Returns - return code.
        If an exception in Powershell is thrown, the function throws PowershellException.
        """
        return Powershell.__run_powershell('-File {file_path} {arguments}'.format(
                                            file_path=file_path,
                                            arguments=arguments))

    @staticmethod
    def __run_powershell(arguments):
        """
        Opens sub-process of Powershell.exe, and waits for it to finish execution.
        Returns - return code.
        Parses the Powershell execption, and throws PowershellExecption.
        """
        execution_line = "{powershell_exe} -ExecutionPolicy {execution_policy} {flags} {arguments}"
        extra_flags = '-NonInteractive -NoLogo'

        formated_execution_line = execution_line.format(
            powershell_exe=consts.POWERSHELL_EXE_PATH,
            execution_policy=consts.DEFAULT_EXECUTION_POLICY,
            flags=extra_flags,
            arguments=arguments)

        process = subprocess.Popen(formated_execution_line,
                                   stderr=subprocess.PIPE,
                                   cwd=os.getcwd())
        
        return_code = process.wait()
        error = process.stderr

        Powershell.__parse_error(error.read())

        return return_code

    @staticmethod
    def __parse_error(stderr):
        """ Parses the stderr, and throws PowershellExecption. """
        
        if stderr:
            raise PowershellException(stderr.decode())

