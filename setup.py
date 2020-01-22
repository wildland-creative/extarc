import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="extarc", # Replace with your own username
    version="0.0.1",
    author="Josh P. Sawyer",
    author_email="josh.p.sawyer@gmail.com",
    description="A collection of functions for extending ESRI's arcpy module. Mostly utility or helper functions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joshpsawyer/arcutils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)