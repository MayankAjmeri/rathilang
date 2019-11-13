#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Rathilang setup script."""

from setuptools import setup

__VERSION__ = "0.1.0"

if __name__ == "__main__":
    setup(
        name="rathilang",
        version=__VERSION__,
        description="A brainfuck derivative based on the the characteristics of Aashutosh Rathi",
        license="MIT",
        keywords="esoteric programming language brainfuck",
        author="Pushkar Patel",
        author_email="thepushkarp@gmail.com",
        url="https://github.com/thepushkarp/rathilang",
        py_modules=["rathilang", "rathilang.cli", "rathilang.interpreter", "setup"],
        install_requires=["ply"],
        entry_points={"console_scripts": ["rathilang = rathilang.cli:main"]},
        classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: Implementation :: PyPy",
        ],
        packages=["rathilang"],
    )
