import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="api_eventbridge_lambda",
    version="0.0.1",

    description="Microservice pattern for event driven application developed and deployed via AWS CDK using AWS Code Pipeline",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="Abhishek Bose",

    package_dir={"": "api_eventbridge_lambda"},
    packages=setuptools.find_packages(where="api_eventbridge_lambda"),

    install_requires=[
        "aws-cdk.core==1.56.0",
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
