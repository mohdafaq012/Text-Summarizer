import setuptools

with open("README.md", "r", encoding="utf-8") as f:     # reading readme file
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "mohdafaq012"            # github user-name
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "mohdafaq5539@gmail.com"

# Final Code for local package setup

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)

# it will look for constructor file every folder and it will install it as my local package
