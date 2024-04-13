from setuptools import setup


setup(
    name="pytha",
    version="0.1",
    description="PYTHA is a Python-based directory fuzzer tool designed to aid in the discovery of hidden or sensitive directories and files on web servers. It uses an asynchronous approach for efficient scanning and supports various customization options.",
    packages=["pytha"],
    entry_points={"console_scripts": ["pytha=pytha.main:main"]},
    install_requires=["aiofiles", "colorama", "httpx"]
)
