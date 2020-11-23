from setuptools import setup

setup(
    name="pokepython",
    version="0.01",
    python_requires='>=3.7',
    packages=["pokepython"],
    install_requires=[
        "tk",
        "pygame",
    ],
    entry_points={'console_scripts': ['pokepython=pokepython.game:main']},
)
