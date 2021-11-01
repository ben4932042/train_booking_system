from setuptools import setup
setup(
    name = "src",
    version = "0.0.0",
    description = "coustom packages install",

    author = "Ben Liu",

    packages = [
        'src',
        'src/model',
        ],
    include_package_data = True,
    platforms = "any",
    install_requires = [],

    scripts = [],
)
