from setuptools import setup, find_packages

VERSION = '0.1.0'
DESCRIPTION = 'Websiteを簡単にコピーしてくれるパッケージです'

setup(
    name="WebSite-Copy-Python",
    version=VERSION,
    author="Zrpy(original: meow)",
    description=DESCRIPTION,
    long_description=DESCRIPTION
    long_description_content_type="text/markdown",
    install_requires=[
        "beautifulsoup4>=4.13.4",
        "requests>=2.32.4",
    ],
    keywords=['python', 'website', 'clone', 'copy', 'cloning'],
    url="https://github.com/zrpy/WebSite-Copy-Python/",
    project_urls={
        "Source Code": "https://github.com/meowkawaiijp/Discord.py-Plus",
    },
)
