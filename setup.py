#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
  readme = readme_file.read()

requirements = [
  'numpy',
  'scipy',
  'SimpleITK==1.2.4',
  'torch>=1.7',
  'torchvision',
  'tqdm',
  'torchio==0.18.29',
  'pandas',
  'pylint',
  'torchsummary',
  'scikit-learn==0.23.1',
  'pickle5==0.0.11',
  'setuptools',
  'seaborn',
  'pyyaml',
  'openslide-python',
  'scikit-image',
  'matplotlib',
  'requests==2.25.0',
  'pyvips',
  'torchviz',
  'pytest',
  'pytest-azurepipelines'
]

setup(
  name='GANDLF',
  version='0.0.7-dev', # NR: non-release; this should be changed when tagging
  author="Ujjwal Baid, Megh Bhalerao, Caleb Grenko, Sarthak Pati, Siddhesh Thakur", # alphabetical order
  author_email='software@cbica.upenn.edu',
  python_requires='>=3.6',
  packages=find_packages(),
  scripts=['gandlf_run', 'gandlf_constructCSV', 'gandlf_collectStats', 'gandlf_patchMiner'],
  classifiers=[
    'Development Status :: 1 - Planning',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: BSD License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
  description=(
    "Segmentation/regression/classification using various DL architectures using PyTorch."
  ),
  install_requires=requirements,
  license="BSD-3-Clause License",
  long_description=readme,
  long_description_content_type='text/markdown',
  include_package_data=True,
  keywords='semantic, segmentation, regression, classification, brain, breast, liver, lung, augmentation',
  zip_safe=False,
)

import os
## submodule update
os.system('git submodule update --init --recursive')

## windows vips installation
if os.name == 'nt': # proceed for windows
  from pathlib import Path
  if not Path('./vips/vips-dev-8.10/bin/libvips-42.dll').exists(): # download and extract if main dll is absent
    print('Downloading and extracting VIPS for Windows')
    import requests, zipfile, io
    r = requests.get('https://github.com/libvips/libvips/releases/download/v8.10.2/vips-dev-w64-all-8.10.2.zip')
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall('./vips')
