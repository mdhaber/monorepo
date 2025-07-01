# package1/__init__.py (can be empty or contain initialization code)


from importlib.metadata import version
from package1._code import *  # noqa: F403

__version__ = version("monorepo_package1")
