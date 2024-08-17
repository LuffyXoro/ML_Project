# Responsible for maintaining ML packages
# Like we use pip install for packages/libraries in python 

from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]: 
    '''This function will return the list of requirements '''

    HYPEN_E_DOT='-e .'
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements: # type: ignore
            requirements.remove(HYPEN_E_DOT)
    return requirements
setup(
    name='ML_PROJECT',
    version='0.0.1',
    author="Rudra Singh",
    author_email='rudra.raghav1212@gamil.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)