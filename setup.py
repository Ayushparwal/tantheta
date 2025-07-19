from setuptools import setup, find_packages

setup(
    name="tantheta",
    version="0.1.0",
    description="A lightweight math library for symbolic calculus, algebra, trigonometry, and statistics",
    long_description="tantheta is a Python package that simplifies solving symbolic math problems like calculus, algebra, trigonometric equations, and statistics. Built on SymPy.",
    long_description_content_type="text/markdown",
    author="Ayush Parwal",
    author_email="ayushparwal777@gmail.com",
    url="https://github.com/ayushparwal/tantheta",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "sympy>=1.12",
    ],
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires='>=3.6',
)
