from setuptools import setup, find_packages
import os
from iancupy_data import download_file

# Download data
download_file.get_dss_image()
download_file.get_m4()

NAME = 'iancupy_data'
# VERSION should be PEP440 compatible (https://www.python.org/dev/peps/pep-0440/)
VERSION = '0.0.dev1'

setup(name=NAME,
      version=VERSION,
      description='Data preparation for IANCU Python exercise',
      install_requires=['astropy', 'astroquery'],
      author='Cheng-Chung Chen, PoShih Chiang, Yi-Hao Su',
      author_email='yhsu@astro.ncu.edu.tw',
      license='MIT',
      packages=find_packages(),
      url='https://github.com/Astrohackers-TW/IANCUPyData.git',
      long_description='',
      zip_safe=False,
)
