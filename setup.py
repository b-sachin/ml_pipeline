from setuptools import setup, find_packages
from typing import List

# Declaring variables for setup function
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Sachin B."
DESCRIPTION = "This project is to predict median housing price"
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list() -> List[str]:
    """
    Description: This function is going to return list of requirement mention in requirment.txt file

    return this function is going to return a list which contain name of libraries mentioned in requirment.txt file

    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    packages= find_packages(),
    install_requires = get_requirements_list()
)