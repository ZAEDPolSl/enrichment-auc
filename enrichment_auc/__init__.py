"""Single cell enrichment analysis via GMM"""
import os

try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata

if os.environ.get("READTHEDOCS") == "True":
    import toml

    dirname = os.path.dirname(__file__)
    with open(os.path.join(dirname, "../pyproject.toml")) as f:
        __version__ = toml.load(f)["tool"]["poetry"]["version"]
else:
    __version__ = importlib_metadata.version(__name__)


__all__ = [
    "__version__",
]
