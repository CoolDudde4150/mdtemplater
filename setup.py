import setuptools

setuptools.setup(
    name="mdtemplater",
    version="0.1",
    licence="MIT",
    description="Creates a markdown file for note taking",
    author="CoolDudde4150",
    url="https://github.com/CoolDudde4150/coursetemplater",
    download_url="https://github.com/CoolDudde4150/coursetemplater/archive/v0.1.tar.gz",
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": ["mdtemplater = mdtemplater.templater:main"]},
)
