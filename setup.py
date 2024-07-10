from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tourism_site/__init__.py
from tourism_site import __version__ as version

setup(
	name="tourism_site",
	version=version,
	description="Hotel booking and tour",
	author="yogenterprise_solutions",
	author_email="yoger@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
