from setuptools import setup, find_packages  # type: ignore

setup(
    name="pdf_qa_agent",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "openai==1.35.13",
        "pypdf2==3.0.1",
        "slack-sdk==3.31.0",
        "python-dotenv==1.0.1",
    ],
    entry_points={
        "console_scripts": [
            "pdf_qa_agent=src.main:main",
        ],
    },
    author="Sainath Ramanathan",
    description="An AI agent that answers questions from PDF documents and posts results to Slack",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rksainath/pdf-qa-agent",
    python_requires=">=3.7",
)
