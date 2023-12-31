from setuptools import setup, find_packages

setup(
    name="lyzr",
    version="0.1.5",
    author="lyzr",
    description="",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8.1, <3.12",
    install_requires=[
        "openai>=0.28.1",
        "litellm>=0.13.1",
        "llama-index>=0.8.61",
        "langchain>=0.0.330",
        "python-dotenv>=1.0.0",
        "tiktoken>=0.5.1",
        "pdfminer-six==20221105",
        "lancedb==0.3.3",
        "beautifulsoup4==4.12.2",
        "docx2txt==0.8",
        "playwright==1.39.0",
        "pytest-playwright==0.4.3",
        "pandas==2.1.2",
        "plotly==5.18.0",
        "scikit-learn==1.3.2",
        "statsmodels==0.14.0",
    ],
)
