"""collection of pip api functions"""

import importlib.metadata

def get_package_version(package_name):
    try:
        version = importlib.metadata.version(package_name)
        return version
    except importlib.metadata.PackageNotFoundError:
        return None
