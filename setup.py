import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.cleanslatebuddy',
      version='1.0',
      description=('Get help preparing expungement petitions'),
      long_description=u'# Clean Slate Buddy\r\n\r\nSkip the _really_ tedious parts of filling out Expungement petitions. \r\n\r\nUse this Docassemble guided interview to automatically generate petitions\r\nfor expungements and sealings.\r\n\r\nYou still have to enter the records you want to expunge by hand, but this interview\r\nwill fill in the required petitions for you. \r\n\r\n',
      long_description_content_type='text/markdown',
      author='Nate Vogel',
      author_email='nvogel@clsphila.org',
      license='The MIT License',
      url='https://docassemble.clsphila.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/cleanslatebuddy/', package='docassemble.cleanslatebuddy'),
     )

