#coding=utf-8
from setuptools import setup

setup(
    author="CrazyJUms",
    author_email ="15959963313@163.com",
    description="This is a utility, writen by CrazyJUms",
    url="https://github.com/crazyjums/my_utility",
    name="utility",
    version="1.0",
    packages=['utility'],
    install_requires=[
        "requests>=2.23.0",
        "bs4>=0.0.1",
        "lxml>=4.5.0"
                     ],
    exclude_package_date={'':['.gitignore'], '':['dist'], '':'build', '':'utility.egg.info'},
)