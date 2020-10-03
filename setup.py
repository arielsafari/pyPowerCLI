import re
import setuptools


with open(r"pyPowerCLI\__init__.py", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)


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
