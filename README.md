# arcutils - for python 2.x

This repository contains python functions for my most often repeated tasks, e.g. getting new scratch feature classes in a scratch gdb, or getting certain projections. It uses the arcpy module which ships with ArcMap Desktop 10.x and as such may not be compatible with ArcGIS Pro. [arcutilspro](https://github.com/joshpsawyer/arcutilspro) is an ArcGIS Pro compatible version.

To install, clone the submodule into your src directory for your project. It's structured so that it will be importable as a subdirectory, e.g.

```
from arcutils import arcutils as au
```
Alternatively, if your project is destined for github, you can add this project as a sub-module. From the git command line, navigate to your project (repo must be initialized) and type:

```
> git submodule add https://github.com/joshpsawyer/arcutils.git
```

This will add the latest commit for the master branch of `arcutils` as a subdirectory. Read https://git-scm.com/book/en/v2/Git-Tools-Submodules to learn more about working with submodules.
