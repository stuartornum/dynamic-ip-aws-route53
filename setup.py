from setuptools import setup

setup(
    # Application name:
    name="dynamic-ip-aws-route53",

    # Version number (initial):
    version="0.0.1",

    # Application author details:
    author="Stuart Munro",

    # Packages
    packages=["dynamic-ip-aws-route53"],

    # Executables
    scripts=['dynamic-ip-aws-route53/dynamic-route53'],

    # Details
    url="https://github.com/stuartornum/dynamic-ip-aws-route53",

    # license="LICENSE.txt",
    description="Command line tool to update a dynamic IP to Route53",

    # Dependent packages (distributions)
    install_requires=[
        "boto3==1.4.3"
    ],

    license = "MIT",

    platforms = "Posix; MacOS X",

    classifiers = ["Intended Audience :: Developers",
                   "License :: OSI Approved :: MIT License",
                   "Topic :: Internet"],
)
