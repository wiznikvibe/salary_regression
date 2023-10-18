from setuptools import find_packages, setup
from typing import List 

def get_requirements(file_path: str)-> List[str]:

    HYPEN_E_DOT = "-e ."
    requirements = []
    with open(file_path) as file_obj:
        requirement_list = file_obj.readlines()
        requirement_list = [requirement.replace("\n", "") for requirement in requirement_list]
        if HYPEN_E_DOT in requirement_list:
            requirement_list.remove(HYPEN_E_DOT)

    return requirements


setup(
    name="salary_prediction",
    version="0.0.1",
    description="Salary Prediction Using Multiple Features",
    author="Nikhil",
    author_email="nikhilshetty00@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)