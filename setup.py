# this will find all the packages installed in the entire project
from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return a list of requirements

    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("/", " ") for req in requirements]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements


# write the metadata about the entire project
setup(
name = "mlproject"
version = '0.0.1'
author = 'Mizan'
author_email = "mizanur55@hotmail.com"
# this will install all the packages in from every folder with __init__ 
packages = find_packages(), 
# mention all the requirements you want
# you want to create a function with a parth here since you might 
# have 100s of requirements
install_requires = get_requirements('requirements.py')
)
