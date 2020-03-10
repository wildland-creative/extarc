# extarc - Utility functions for `arcpy`

[![Build Status](https://travis-ci.com/dorkwood/extarc.svg?branch=master)](https://travis-ci.com/dorkwood/extarc)
[![Latest pypi version](https://img.shields.io/pypi/v/extarc)](https://pypi.org/project/extarc/)

This repository contains python functions for commonly repeated tasks, e.g. getting new scratch feature classes in a scratch gdb, or getting certain projections. It's named extarc because it... **ext**ends **arc**py. It also sounds like a cool ship from [The Expanse](https://en.wikipedia.org/wiki/The_Expanse_(TV_series)) which you should really watch. It utilizes the `arcpy` module which ships with ArcMap Desktop / ArcGIS Pro and so it's assumed that your python environment has access to these modules. That is, if you can't `import arcpy` already, why are you trying to use a helper library? Currently, arcpy is _not_ part of requirements.txt because it's not clear whether it will pass a CI check.

## Installation

### pip

You can install the latest stable version with pip via:

```bash
pip install extarc
```

And if you want to be on the bleeding edge of development, get the latest version from github:

```bash
pip install --editable=git+https://github.com/dorkwood/extarc.git#egg=pyhere
```

### conda

Not in conda, yet - just install it from pip in your environment.

## Usage

```python
import extarc as ea
```
