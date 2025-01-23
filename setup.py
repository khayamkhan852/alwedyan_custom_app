from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in alwedyan_custom_app/__init__.py
from alwedyan_custom_app import __version__ as version

setup(
	name="alwedyan_custom_app",
	version=version,
	description="Custom Frappe ERPNext application for Alwedyan",
	author="Alwedyan",
	author_email="khayamkhan852@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)