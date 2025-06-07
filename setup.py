from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    try:
        with open('requirements.txt', 'r') as file:
            requirement_list = [
                line.strip() for line in file.readlines()
                if line.strip() and line.strip() != '-e .'
            ]
        return requirement_list
    except FileNotFoundError:
        print("requirements.txt file not found. Make sure it exists!")
        return []

try:
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ""

setup(
    name="Role based Rag Chatbot",
    version="0.1.0",
    description="Starter project for the RPC-01: Internal Chatbot with Role Based Access Control",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="ds-rpc-01",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=get_requirements(),
)
