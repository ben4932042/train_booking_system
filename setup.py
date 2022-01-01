from setuptools import setup
setup(
    name = "src",
    version = "0.0.0",
    description = "coustom packages install",

    author = "Ben Liu",

    packages = [
        'src',
        'src/model',
        'src/seat_strategy_factory',
        ],
    include_package_data = True,
    platforms = "any",
    install_requires = [],

    scripts = [],
)
