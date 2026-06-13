from setuptools import find_packages, setup

from os import path
top_level_directory = path.abspath(path.dirname(__file__))
with open(path.join(top_level_directory, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='phonebox_plugin',
    version='1.0.0',
    url='https://gitlab.olson-network.com/telephony/phonebox_plugin',
    description='A phone numbers management plugin for NetBox (4.5/4.6).',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Isaiah Olson',
    author_email='insignia96@gmail.com',
    install_requires=[],
    packages=find_packages(),
    python_requires='>=3.12',
    license='MIT',
    include_package_data=True,
    keywords=['netbox', 'netbox-plugin', 'plugin'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
    ],
)
