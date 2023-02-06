import os

from setuptools import setup

requires = open("requirements.txt", "r").readlines() if os.path.exists("requirements.txt") else open("./arizon_usb_driver.egg-info/requires.txt", "r").readlines()
print("#-------------------    ", str(os.listdir("./")))
setup(
    name="arizon-usb-driver",
    version="0.1",
    author="davidliyutong",
    author_email="davidliyutong@sjtu.edu.cn",
    description="Driver for Arizona USB Pressure Sensor",
    packages=[
        "arizon_usb_driver",
    ],
    python_requires=">=3.7",
    install_requires=requires,
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown"
)