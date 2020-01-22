# extarc - Utility functions for **ext**ending `**arc**py`

This repository contains python functions for commonly repeated tasks, e.g. getting new scratch feature classes in a scratch gdb, or getting certain projections. It utilizes the `arcpy` module which ships with ArcMap Desktop / ArcGIS Pro and so it's assumed that your python environment has access to these modules. That is, if you can't `import arcpy` already, why are you trying to use a helper library?

To install, clone or copy the submodule into the directory where your python code lives for your project. It's structured so that it will be importable as a subdirectory, e.g.

```python
import extarc as au
```

Alternatively, if your project is destined for github, you can add this project as a sub-module. From the `git` command line, navigate to your project (repo must be initialized) and type:

```bash
> git submodule add https://github.com/joshpsawyer/extarc.git
```

This will add the latest commit for the master branch of `extarc` as a subdirectory. Read https://git-scm.com/book/en/v2/Git-Tools-Submodules to learn more about working with submodules. You'll be able to update the arcutils module to later versions without maintaining a distinct copy.
