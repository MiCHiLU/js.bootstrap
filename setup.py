from setuptools import setup, Command, find_packages
import os
import sys

version = '3.3.2'

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.rst')
    + '\n' +
    read('js', 'bootstrap', 'test_bootstrap.txt')
    + '\n' +
    read('CHANGES.txt'))

install_requires = [
    'fanstatic',
    'js.jquery',
    'setuptools',
]

# We use tox to test fanstatic across python versions. We would like to
# declare the python-version-based dependency on the "shutilwhich" package
# like this:
#
# if sys.version_info < (3, 3):
#     install_requires.append('shutilwhich')
#
# Unfortunately, we can't do this because of how tox works; if not listing
# shutilwhich as a dependency, the py33 tests fail when filling the fanstatic
# compiler and minifier registries.
#
# We choose to list shutilwhich as a dependency in order to be able to use
# tox. This is not an ideal situation, but the shutilwhich code is harmless on
# python3.3.

if sys.version_info < (2, 7):
    install_requires.append('argparse')

tests_require = [
    'pytest >= 2.3',
]


class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys
        import subprocess
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)

setup(
    classifiers=[
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Development Status :: 5 - Production/Stable'
    ],
    name='js.bootstrap',
    version=version,
    description="fanstatic twitter bootstrap.",
    long_description=long_description,
    keywords='fanstatic twitter bootstrap redturtle',
    author='RedTurtle Developers',
    url='https://github.com/RedTurtle/js.bootstrap',
    author_email='sviluppoplone@redturtle.it',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
    },
    cmdclass={'test': PyTest},
    entry_points={
        'fanstatic.libraries': [
            'bootstrap = js.bootstrap:library',
            ],
        },
    )
