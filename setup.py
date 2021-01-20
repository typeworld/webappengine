from setuptools import setup, find_packages
import platform

WIN = platform.system() == "Windows"
MAC = platform.system() == "Darwin"
LINUX = platform.system() == "Linux"

install_requires = [  # I get to this in a second
    "google-cloud-ndb",
]

setup(
    name="webappengine",  # How you named your package folder (MyLib)
    version="0.1.0",
    license="apache-2.0",
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description="""Abstraction layer on top of Python-NDB for use in Google App Engines. It’s mainly used for https://type.world and is therefore not generally supported at this point.""",  # Give a short description about your library
    author="Type.World",  # Type in your name
    author_email="hello@type.world",  # Type in your E-Mail
    url="https://github.com/typeworld/webappengine",
    # Provide either the link to your github or to your website
    keywords=["gae"],  # Keywords that define your package best
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 3 - Alpha",
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        # as the current state of your package
        "Environment :: Console",
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: Apache Software License",  # Again, pick a license
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    package_dir={"": "Lib"},
    packages=find_packages("Lib"),
    include_package_data=True,
)
