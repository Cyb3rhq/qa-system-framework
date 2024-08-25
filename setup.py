# Copyright (C) 2015-2023, Cyb3rhq Inc.
# Created by Cyb3rhq, Inc. <info@wazuh.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
from setuptools import setup, find_namespace_packages
import shutil
import glob


setup(
    name='cyb3rhq-qa-framework',
    version='1.0.0',
    description='Cyb3rhq testing utilities to help programmers automate tests',
    url='https://github.com/cyb3rhq/cyb3rhq-qa-framework',
    author='Cyb3rhq',
    author_email='hello@wazuh.com',
    license='GPLv2',
    package_dir={'': 'src'},
    packages=find_namespace_packages(where='src'),
    zip_safe=False
)

# Clean build files
shutil.rmtree('dist')
shutil.rmtree('build')
shutil.rmtree(glob.glob('src/*.egg-info')[0])
