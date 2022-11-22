from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in xtc_mobile_api/__init__.py
from xtc_mobile_api import __version__ as version

setup(
	name="xtc_mobile_api",
	version=version,
	description="API to create picklist from mobile",
	author="GreyCube Technologies",
	author_email="admin@greycube.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
