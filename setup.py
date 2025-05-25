# this file responsable to build my ML application as package .building our application as package
from setuptools import setup, find_packages
from typing import List 


HYPEN_E_DOT = '-e .'
def get_requiremnts(file_path:str)->List[str]:
    """
    this function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements





setup (
name= "mlproject",
version= "0.0.1",
author= "Achraf Bogryn",
author_email= "achrafbogryn12345@gmail.com",
packages= find_packages(),
install_requires =  get_requiremnts('requirements.txt')    
     
     
     )