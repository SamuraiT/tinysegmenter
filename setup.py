from distutils.core import setup, Command
import os
import sys

sys.path.append('./tinysegmenter')
sys.path.append('./tests')

def read_file(filename):
    filepath = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), filename)
    if os.path.exists(filepath):
        return open(filepath).read()
    else:
        return ''

class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        import sys,subprocess
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)

setup(
    name = 'tinysegmenter3',
    packages = ['tinysegmenter'],
    version = '0.0.3',
    description = 'Super compact Japanese tokenizer',
    maintainer = 'Tatsuro Yasukawa',
    maintainer_email = 't.yasukawa01@gmail.com',
    url = 'https://github.com/SamuraiT/tinysegmenter',
    license='New BSD',
    long_description = read_file('README.md'),
    cmdclass = {'test':PyTest},
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Environment :: MacOS X",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

