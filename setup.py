from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

from crm_chat_integration import __version__ as version

setup(
    name="crm_chat_integration",
    version=version,
    description="Chat application for frappe",
    author="Abhishek Chougule",
    author_email="abhishek.c@onehash.ai",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)
