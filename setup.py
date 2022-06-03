try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

here = path.abspath(path.dirname(__file__))

setup(
    name='One Line Calculator',
    version='0.0.1',
    description='Calculator that calculates user input and returns a solution.',
    long_description=long_description,
    url='https://github.com/dcapella/one-line-calculator.git',
    author='David Capella',
    author_email='D_Capella@Yahoo.com',
    # license='something',
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        # 'License :: OSI Approved :: something License',
        'Programming Language :: Python :: 3.6.1',
    ],
    keywords='one line calculator simple project',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    # install_requires=[''],
)
