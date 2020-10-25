from setuptools import setup

setup(
    name='Pip-Up',
    verion='0.0.1',
    description='A python 3 package upgrader',
    py_modules=['pip_up'],
    package_dir={'', 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent"
    ],
    install_requires=[

    ],
    extras_require={
        "dev": [
            "python>=3.7"
        ]
    },
    url="https://github.com/letsgogeeky/pip-up",
    author="Ramy Mousa",
    author_email=""
)
