from setuptools import setup, find_packages
import os

version = '1.0a-dev'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

tests_require=[
    'Cheetah', 
    'PasteScript',
    'templer.core'],

setup(name='templer.buildout',
      version=version,
      description="Templer system extensions for buildouts and buildout recipes",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Cris Ewing',
      author_email='cris@crisewing.com',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['templer'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'templer.core',
      ],
      tests_require=tests_require,
      extras_require=dict(test=tests_require),
      entry_points="""
      [paste.paster_create_template]
      recipe = templer.buildout:Recipe
      basic_buildout = templer.buildout:BasicBuildout
      
      [templer.templer_structure]
      bootstrap = templer.buildout.structures:BootstrapStructure
      """,
      )
