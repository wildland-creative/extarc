# extarc - Utility functions for `arcpy`

[![Build Status](https://travis-ci.com/joshpsawyer/extarc.svg?branch=master)](https://travis-ci.com/joshpsawyer/extarc)

This repository contains python functions for commonly repeated tasks, e.g. getting new scratch feature classes in a scratch gdb, or getting certain projections. It's named extarc because it... **ext**ends **arc**py. It also sounds like a cool ship from [The Expanse](https://en.wikipedia.org/wiki/The_Expanse_(TV_series)) which you should really watch. It utilizes the `arcpy` module which ships with ArcMap Desktop / ArcGIS Pro and so it's assumed that your python environment has access to these modules. That is, if you can't `import arcpy` already, why are you trying to use a helper library? Currently, arcpy is _not_ part of requirements.txt because it's not clear whether it will pass a CI check.

## Installation

While you can always just clone this repository into your project, or add it as a submodule via:

```bash
> git submodule add https://github.com/joshpsawyer/extarc.git
```

...it's a much better practice to install it as a module in your python environment - less maintenance, no unnecessary packages in your code. While structured for pypi, it's currently _not_ in the index. You need to install a development build. Anaonda is recommended for environment management, but because Anaconda doesn't _directly_ support this - you need to use pip.

Assuming you have anaconda installed and a target environment, open your command prompt / terminal. If you're installing it to the conda environment `cool-env`, switch to that environment now:

```bash
(base)> conda env activate cool-env
(cool-env)> conda env activate cool-env
```

From the prompt, type:

```bash
(cool-env)> pip install --editable=git+https://github.com/joshpsawyer/extarc.git#egg=extarc
```

The latest master commit will be installed under the package named `extarc-joshpsawyer`. To uninstall, type:

```bash
(cool-env)> pip uninstall extarc-joshpsawyer
```

## Usage

```python
import extarc as ea
```
