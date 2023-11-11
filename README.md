# lyzr

[![PyPI - Version](https://img.shields.io/pypi/v/lyzr-stack.svg)](https://pypi.org/project/lyzr-stack)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/lyzr-stack.svg)](https://pypi.org/project/lyzr-stack)

-----

**Table of Contents**

- [Installation](#installation)
- [Building from Source](#building-from-source)
- [License](#license)

## Installation

You can install the `lyzr` package directly from PyPI:

```console
pip install lyzr
```

## Building from Source

If you prefer to build the `lyzr` package from source, you'll need to have Python installed along with `setuptools` and `wheel`. 

### Steps to Build:

1. Clone the repository or download the source code.
2. Navigate to the root directory of the project (where `setup.py` is located).
3. Run the following commands:

```console
# Ensure setuptools and wheel are installed
pip install setuptools wheel

# Build the package
python setup.py sdist bdist_wheel
```

This will generate a `dist` directory containing the built package files.

### Installing the Built Package:

Once you've built the package, you can install it using pip:

```console
cd dist/
pip install lyzr-[version]-py3-none-any.whl
```

Replace `[version]` with the actual version of the package you have built.

## License

`lyzr` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
