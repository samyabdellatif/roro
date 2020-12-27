import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="roro-samyabdellatif",
    version="1.0.0",
    author="Samy Abdellatif",
    author_email="samiahmed086@gmail.com",
    description="turtle drawing the word RORO",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/samyabdellatif/roro",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)