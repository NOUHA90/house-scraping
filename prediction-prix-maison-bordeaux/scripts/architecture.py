import os
import shutil

def command_list(project_name):
    return [f"mkdir {project_name}",
                f"touch {project_name}/__init__.py",
                f"touch {project_name}/preprocessing.py",
                f"touch {project_name}/pipeline.py",
                f"touch {project_name}/get_data.py",
                f"touch {project_name}/model.py",
                "touch setup.py",
                "mkdir notebooks",
                "mkdir api",
                "mkdir data",
                "mkdir tests",
                "touch tests/test.py",
                "touch api/fast.py",
                "touch README.md",
                "touch requirements.txt",
                "touch Makefile",
                "mkdir scripts"]

def creation_architecture(project_name):
    for element in command_list(project_name):
        os.system(element)
        print(f"Command > {element}")
    print("-"*50)


def writter_file(dict):
    for i in dict:
        with open(i, "w") as filout:
            filout.write(dict[i])
            print(f"Ajout du code dans le fichier {i} :\n{dict[i]}\n")
    print("-"*50)

dictionnaire = {"setup.py" :
"""
from setuptools import setup
   
setup(
   name="prediction",
   version='0.1.0',
   description="This package represent the library of th machine learning",
   author="Nouha EL ABED",
   modules=['prediction'],
   install_requires=['Seaborn'])""",
            "requirements.txt" :
                """
                numpy
                pandas
                seaborn
                plotly
                Scrapy
                streamlit
                fastapi
                selenium
                beautifulsoup4
                matplotlib==3.5.2
                scikit-learn==1.1.1
                pytest
                unittest2""",
            "Makefile" :
                """
                install_requirements:
                    pip install -r requirements.txt
                test:
                    run -m unittest tests/*.py
                """}

creation_architecture(str(input('Please type the name of your package : ')))
writter_file(dictionnaire)
os.system("pip install -r requirements.txt")
shutil.move("architecture.py", "scripts/architecture.py")