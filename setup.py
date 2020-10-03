import re
import setuptools

from pyPowerCLI.install import install_powercli, is_installed

with open(r"pyPowerCLI\__init__.py", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)


# Install PowerCLI on the computer, 
# and validate the installation.
install_powercli()

if not is_installed():
    raise RuntimeError("PowerCLI haven't installed correctly.")


setuptools.setup(
    name="pyPowerCLI",
    version=version,
    author="Ariel Yusim",
    author_email="arielsafari@gmail.com",
    url="https://github.com/arielsafari/pyPowerCLI",
    description="Execute PowerCLI commands and scripts using python.",
    packages=setuptools.find_packages(),
    package_data={'': ['resources/*']}
)
