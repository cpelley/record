#!/usr/bin/env python
# The MIT License (MIT)
#
# Copyright (c) 2013 Carwyn Pelley
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import ConfigParser
from distutils.core import setup, Command
import imp
import os
import sys


class Uninstall(Command):
    """
    Uninstall files generated via setup.py install

    """
    description = 'Uninstall files generated via setup.py install'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        config = ConfigParser.SafeConfigParser()
        config.read([os.path.join(__file__, 'setup.cfg')])

        self.value = 'uninstall.log'
        if config.has_option('install', 'record'):
            self.value = config.get('install', 'record')

    def run(self):
        if os.path.isfile(self.value):
            os.system('cat {0}; cat {0} | xargs rm -rf'.format(
                self.value))
        else:
            print 'Cannot uninstall, uninstall log () does not exist'.format(
                self.value)


def extract_version():
    version = None
    with open('bin/record') as fd:
        for line in fd.readlines():
            if (line.startswith('__version__')):
                version = eval('dict({})'.format(line.strip()))['__version__']
                break
    return version


utility_path = 'bin/record'
record = imp.load_source('record', utility_path)


setup(name='Record',
      version=extract_version(),
      description='Commandline recording facility',
      author='Carwyn Pelley',
      author_email='carwyn.pelley@gmail.com',
      url='https://github.com/cpelley/record',
      scripts=[utility_path],
      cmdclass={'uninstall': Uninstall}
     )
