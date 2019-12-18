import setuptools

long_description = "The package aims to simplify data transfer between different database.";

setuptools.setup(
    name="data2db", # Replace with your own username
    version="0.0.1",
    author="Aman Khandelwal",
    author_email="amanpoke@gmail.com",
    description="Data 2 db Migrator",
    long_description=long_description,
    long_description_content_type="text",
    url="https://github.com/amankhandelwal-ideaspark/data2db",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)