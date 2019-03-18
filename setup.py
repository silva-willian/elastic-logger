from setuptools import setup

setup(
    name='Elastic logger',
    version='1.0.7',
    author='Willian da Silva',
    author_email='silva.willian@outlook.com',
    description='Solution created for segregation of logs for the elasticsearch in python',
    url='https://github.com/silva-willian/elastic-logger',
    license='Apache2',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'

    ],
    packages=['elasticlogger'],
    install_requires=[
        'python-dotenv==0.8.2',
        'jsonpickle==0.9.6',
        'elasticsearch==6.2.0'
    ]
)
