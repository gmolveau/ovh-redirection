import setuptools
from distutils.core import setup

setup(
    name='ovh123',
    version='1.0',
    packages = ['ovh_client'],
    entry_points = {
        'console_scripts': [
            'ovh123 = ovh_client.cli:main']
    }
)

# python3 setup.py sdist bdist_wheel #build your wheel
# pip download -r .././requirements.txt -d "/home/package" #dl all packages
# tar cvfz requirements.tgz /home/package
# tar xvfz requirements.tgz
# pip install my_app.whl -f ./ --no-index --no-deps #install you wheel with local packages