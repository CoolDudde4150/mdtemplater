import setuptools
from importlib_metadata import entry_points

setuptools.setup(
    name="mdtemplater",
    version="0.0.1",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "templater = mdtemplater.templater:main"
        ]
    }
)