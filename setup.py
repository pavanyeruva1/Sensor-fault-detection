from setuptools import find_packages,setup
#from typing import List

def get_req():

    """
    
    this function will return the  list of requirements

    
    """

    requirements_list=[]
    with open("requirements.txt") as file:
        for line in file:
            requirements_list.append(line)
    return requirements_list


setup(


    name="sensor fault Detection",
    version="0.0.1",
    author="pavan yeruva",
    author_email="pavan.yeruva1@gmail.com",
    packages=find_packages(),
    install_requires=get_req()
)
