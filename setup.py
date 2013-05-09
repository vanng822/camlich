
import os

from setuptools import setup, find_packages

from distutils.core import Extension

camlich = Extension('camlich', sources = ['src/camlich.c'])

here = os.path.abspath(os.path.dirname(__file__))

setup(name='camlich',
      version='0.1',
      author='',
      author_email='',
      url='',
      packages=find_packages(),
      test_suite="tests",    
      ext_modules = [camlich],
)