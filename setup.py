import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hypot",
    version="0.1.0",
    author="Patricia Ternes",
    author_email="p.ternesdallagnollo@leeds.ac.uk",
    description="The hypot SWD3 demo package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Intended Audience :: Science/Research/Learning",
    ],
    python_requires=">=3.9",
)
