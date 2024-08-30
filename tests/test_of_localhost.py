"""tests for localhost"""
import time
from tools import pip_api

def test_pip_package_version():
    """Test of get loggs api"""
    start_time = time.time()
    package_name = "requests"
    package_version = pip_api.get_package_version(package_name)
    print(f"test_pip_package_version {package_version} version")
    end_time = time.time()
    runtime = end_time - start_time
    print(f"runtime for test_pip_package_version {runtime} seconds")
    assert package_version >= "2.28.1"
