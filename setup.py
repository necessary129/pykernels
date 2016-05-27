from setuptools import setup

def read(fname):
    with open(fname) as f:
        return f.read()

setup(
    name = "PyKernels",
    version = "0.0.4",
    author = "Wojciech Marian Czarnecki and Katarzyna Janocha",
    author_email = "contact@gmum.net",
    description = "Python library for working with kernel methods in machine learning",
    license = "MIT",
    keywords = "kernel machine learning",
    url = "https://github.com/gmum/pykernels",
    packages=['pykernels'],
    install_requires = ["numpy", "scipy", "scikit-learn"],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Topic :: System :: Operating System Kernels",
        "License :: OSI Approved :: MIT License"
    ],
)
