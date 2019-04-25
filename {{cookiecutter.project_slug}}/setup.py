""" Setup script for the {{ cookiecutter.app_name }} application.

"""
from itertools import chain
from os import walk
from pathlib import Path

from setuptools import find_packages
from setuptools import setup


_config = {
    "name": "{{ cookiecutter.app_name }}",
    "author": "{{ cookiecutter.author_name }}",
    "author_email": "{{ cookiecutter.author_email }}",
    "url": "",
    "package_dir": {"": "src"},
    "packages": find_packages("src"),
    "entry_points": {
        "console_scripts": ("{{ cookiecutter.cli_script }} = {{ cookiecutter.app_name }}.cli:main",),
    },
    "data_files": ("etc/",),
}


def main():
    """ Execute the setup command.

    """
    def file_tree(*dirs):
        """ Recursively list all directories and their file names. """
        items = chain.from_iterable((walk(root) for root in dirs))
        for root, _, files in items:
            yield root, tuple(str(Path(root, name)) for name in files)
        return

    def version():
        """ Get the local package version. """
        namespace = {}
        path = Path("src", _config["name"], "__version__.py")
        exec(path.read_text(), namespace)
        return namespace["__version__"]

    _config.update({
        "data_files": list(file_tree(*_config["data_files"])),  # expand files
        "version": version(),
    })
    setup(**_config)


# Make the script executable.

if __name__ == "__main__":
    raise SystemExit(main())
