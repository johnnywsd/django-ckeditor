import os.path
from distutils.core import setup


def get_source_files():
    for dirname, _, files in os.walk('ckeditor/static/ckeditor/ckeditor/_source'):
        for filename in files:
            yield os.path.join('/'.join(dirname.split('/')[1:]), filename)

setup(
    name='django-ckeditor-updated',
    version='4.2.4',
    description='Django admin CKEditor integration.',
    long_description=open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read() + open('CHANGELOG.rst', 'r').read(),
    author='Piotr Malinski',
    author_email='riklaunim@gmail.com',
    url='https://github.com/riklaunim/django-ckeditor',
    packages=[
        'ckeditor',
    ],
    install_requires=[
        'Django',
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
