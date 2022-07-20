"""The setuptools setup script."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

# Define your dependencies here
requirements = []
setup_requirements = []

setup(
    author="MaisTODOS",
    author_email="devs@maistodos.com.br",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: Portuguese",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Lib para KYC, via aws",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords="pyrekognition",
    name="pyrekognition",
    packages=find_packages(include=["pyrekognition", "pyrekognition.*"]),
    setup_requires=setup_requirements,
    url="https://github.com/MaisTodos/pyrekognition",
    version="0.0.1",
    zip_safe=False,
)
