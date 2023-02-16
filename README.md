# PyPatchwork
PyPatchwork is a Python library to access the [Patchwork](http://jk.ozlabs.org/projects/patchwork/) REST API.

## Installation
This package can be installed from [Python Package Index(PyPi)](https://pypi.org/project/PyPatchwork/).

```bash
$ pip install PyPatchwork
```

## Usage

```python
from patchwork import Patchwork

# Create patchwork object
pw = Patchwork('https://patchwork.kernel.org')

# Create patchwork object with access token
pw = Patchwork('https://patchwork.kernel.org', 'your_access_token')
```

## Examples

```python
from patchwork import Patchwork

pw = Patchwork('https://patchwork.kernel.org')

# Search project
projects = pw.get_all_projects()
for project in projects:
    if project.name == "Bluetooth":
        break

# Get Project
project = pw.get_project(395)

# Get Series
series = pw.get_series(565705)

```

## Class references

See [Patchwork Classes](https://pypatchwork.readthedocs.io/en/latest/classes.html) for the details of class

## Note

* Only support the basic GET method
* Need to improve the Pagination such as slice and get page
* Need to support query parameters
* Need to support more methods like PUT, and PATCH
* more to come