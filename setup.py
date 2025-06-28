from setuptools import setup, find_packages

setup(
    name="akedly-client",
    version="0.1.0",
    description="Unofficial Akedly OTP API Client",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="ahmed elattar",
    author_email="ahmeddelattarr@outlook.com",
    url="https://github.com/ahmeddelattarr/Akedly_Client",
    packages=find_packages(),
    install_requires=["requests", "python-dotenv"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)

