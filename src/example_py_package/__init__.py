from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("example-py-package")
except PackageNotFoundError:
    # package is not installed
    pass
