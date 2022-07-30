from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="uwuipy",
    version="0.1.1",
    author="Cuprum77",
    description="Allows the easy implementation of uwuifying words for applications like Discord bots and websites",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/Cuprum77/uwuipy",
    package_dir={"": "src"},
    packages=find_packages(where="src")
)