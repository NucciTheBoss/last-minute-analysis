#!/usr/bin/env python3

from setuptools import setup, find_packages


setup(
    name="analysis",
    version="0.1.0",
    description="Podunk scripts for analyzing data.",
    author="Jason C. Nucciarone",
    author_email="jason.nucciarone@canonical.com",
    license="GPL-3.0",
    python_requires=">=3.8",
    packages=find_packages(
        where="src",
    ),
    package_dir={"": "src"},
    entry_points={"console_scripts": ["analysis=analysis.main:main", "fragmentor=fragmentor.main:main", "graphgen=graphgen.main:main"]},
    install_requires=[
        "progress",
        "click",
        "Faker",
        "matplotlib",
        "numpy",
    ],
    keywords=[
        "hpc",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Environment :: Console",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)