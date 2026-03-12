from setuptools import setup, find_packages

setup(
    name="openclaw-coder",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai>=1.0.0",
        "python-dotenv",
        "pydantic>=2.0.0",
    ],
    author="OpenClaw Maintainers",
    description="Automated Python code generation with OpenClaw agents",
)
