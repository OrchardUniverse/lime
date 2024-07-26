from setuptools import setup, find_packages

setup(
    name="orchard-lime",
    version="0.1.0",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        # Add your package dependencies here
    ],
    author="Orchard Universe",
    description="The free model service for anonymous users.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/OrchardUniverse/lime",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'lime=lime.main:main',
        ],
    },
)
