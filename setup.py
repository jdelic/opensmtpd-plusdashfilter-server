#!/usr/bin/env python -u
import os
import re

from setuptools import setup, find_packages
from pip.req import parse_requirements
from pip.download import PipSession

with open("plusdashfilter/__init__.py", "rt", encoding="utf-8") as vf:
    lines = vf.readlines()

_version = "0.0.0+local"
for l in lines:
    m = re.match("version = \"(.*?)\"", l)
    if m:
        _version = m.group(1)

_packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])
pipsession = PipSession()
reqs_generator = parse_requirements(os.path.join(os.path.abspath(os.path.dirname(__file__)), "requirements.txt"),
                                    session=pipsession)  # prepend setup.py's path (make no assumptions about cwd)
reqs = [str(r.req) for r in reqs_generator]

setup(
    name='net.maurus.smtpplusdashfilter',
    entry_points = {
        "console_scripts": [
            "plusdashfilter = plusdashfilter.server:main"
        ]
    },
    version=_version,
    packages=_packages,
    install_requires=reqs,
)
