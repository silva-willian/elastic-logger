from setuptools import setup

setup(
    name='Elastic logger',
    version='0.0.1',
    author='Willian da Silva',
    author_email='silva.willian@outlook.com.br',
    install_requires=[
        'python-dotenv==0.8.2',
        'jsonpickle==0.9.6',
        'elasticsearch==6.2.0'
    ]
)
