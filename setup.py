from distutils.core import setup

with open('requirements.txt') as f:
    requirements = [l.strip() for l in f]

setup(
    name='names',
    version='0.1',
    packages=['names'],
    author='Lucy Wyman',
    author_email='wyman.lucy@gmail.com',
    url='https://github.com/lucywyman/names',
    install_requires=requirements,
    package_data={'cah': ['requirements.txt', 'README.md', 'LICENSE']}
)
