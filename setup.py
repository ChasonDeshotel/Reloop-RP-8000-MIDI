import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Reloop-RP-8000-MIDI"
    , version="0.0.1"
    , author="Chason Deshotel"
    , author_email="me@chasondeshotel.com"
    , description="Reloop RP-8000 MIDI interface"
    , long_description=long_description
    , long_description_content_type="text/markdown"
    , url="https://github.com/ChasonDeshotel/Reloop-RP-8000-MIDI"
    , packages=setuptools.find_packages()
    , classifiers=[
        "Programming Language :: Python :: 3"
        "License :: OSI Approved :: GNU GPLv3"
        "Operating System :: OS Independent"
    ]
    , python_requires='>=3.7'
)
