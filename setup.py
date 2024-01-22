from setuptools import find_packages, setup
from typing import List

HYFUN = "-e ."

def get_requirement(file_path:str)->List[str]:
    '''

    This function will return the List of Required packages

    '''
    requiements = []

    with open(file_path) as f:
        requiements = f.readlines()
        requiements = [req.replace("\n","") for req in requiements]

        if HYFUN in requiements:

            requiements.remove(HYFUN)

    
    return requiements


setup(
    name="MLProject",
    version="0.0.1",
    author="Chander",
    author_email="cmnokhwal82210@gmail.com",
    packages=find_packages(),
    include_dirs = get_requirement("requirements.txt")
)