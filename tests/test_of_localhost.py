"""tests for localhost"""
import time
from tools import pip_api

def test_pip_package_requests_version():
    """Test that the pip package requests version"""
    start_time = time.time()
    package_name = "requests"
    package_version = pip_api.get_package_version(package_name)
    print(f"test_pip_package_requests_version {package_version} version")
    end_time = time.time()
    runtime = end_time - start_time
    print(f"runtime for test_pip_package_requests_version {runtime} seconds")
    assert package_version >= "2.28.1"

def test_pip_package_urllib3_version():
    """Test that the pip package urllib3 version"""
    start_time = time.time()
    package_name = "urllib3"
    package_version = pip_api.get_package_version(package_name)
    print(f"test_pip_package_urllib3_version {package_version} version")
    end_time = time.time()
    runtime = end_time - start_time
    print(f"runtime for test_pip_package_urllib3_version {runtime} seconds")
    assert package_version >= "1.26.13"
