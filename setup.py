import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="extarc",
    version="0.0.1",
    author="Josh P. Sawyer",
    author_email="josh.p.sawyer@gmail.com",
    license="MIT",
    description="A collection of functions for extending ESRI's arcpy module. Mostly utility or helper functions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dorkwood/extarc",
    packages=setuptools.find_packages(),
    classifiers=[
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=2.7'
)