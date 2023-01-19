from setuptools import setup, find_packages
from pathlib import Path
from nomiden import __version__


setup(
    name="nomiden",
    version=__version__,
    description="A Python package to extract information from Indonesian ID Number (NIK, KK)",
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/divakartika/nomiden",
    author="Diva K",
    author_email="diva@algorit.ma",
    license="MIT",
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*", "*npwp.*"]),
    include_package_data=True,
    install_requires=["pandas"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System" " :: OS Independent",
    ],
    # entry_points={
    #     "console_scripts": [
    #         "tq=taskquant.__main__:main",
    #     ]
    # },
    python_requires=">=3.9"
)