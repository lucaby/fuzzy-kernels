import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fuzzy-kernels",
    version="0.0.1",
    author="Lucas Yau, Jorge Guevara, Roberto Hirata",
    author_email="",
    description="Kernel applications on fuzzy sets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ruhaker/fuzzy-kernels",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)