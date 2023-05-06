from setuptools import setup, find_packages

with open("./README.md", "r") as f:
    long_description = f.read()

# Version
# Info: https://packaging.python.org/guides/single-sourcing-package-version/
# Example: https://github.com/pypa/warehouse/blob/64ca42e42d5613c8339b3ec5e1cb7765c6b23083/warehouse/__about__.py
meta_package = {}
with open("./margatsni/__version__.py") as f:
    exec(f.read(), meta_package)


setup(
    name="margatsni",
    version=meta_package["__version__"],
    description="Minet only for Instagram",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/MiguelLaura/margatsni",
    license="MIT",
    author="Miguel Laura",
    keywords="webmining",
    python_requires=">=3.7",
    packages=find_packages(exclude=["ftest", "scripts", "test"]),
    install_requires=["minet==1.0.0a13"],
    entry_points={"console_scripts": ["margatsni=margatsni.cli.__main__:main"]},
    zip_safe=True,
)
