# nomiden

## What is it?

**nomiden** is a Python package that provides information extraction from Indonesian ID Numbers, i.e. personal ID number NIK (Nomor Induk Kependudukan) and family ID number KK (Kartu Keluarga). This package is intended to help users dealing with population and client data to auto-complete missing data or add valuable information, given the ID numbers. Information regarding identity numbers refers to Article 33 of Government Regulation Number 37 of 2007.

## Main Features
Here are the things that **nomiden** can do for you:

  - Retreive regional information 
    - Province
    - City
    - District
  - Retreive gender information (NIK only)
  - Retreive birth information (NIK only)
    - Age
    - Birthday (e.g. 15 June 2000)
    - Birth date
    - Birth month
    - Birth year
    - Birth in datetime
  - Retreive registration information (KK only)
    - Registration day (e.g. 15 June 2000)
    - Registration date
    - Registration month
    - Registration year
    - Registration in datetime
  - Registration order
  - Complete information in a dictionary

## Where to get it
The source code is currently hosted on GitHub at: [https://github.com/divakartika/nomiden](https://github.com/divakartika/nomiden)

**nomiden** is available at the [Python Package Index (PyPI)](https://pypi.org/project/nomiden/).

```sh
pip install nomiden
```

## Requirements & Dependencies
- Python 3.7 and above
- [Pandas - Supports data-related operations](https://pandas.pydata.org)

## License
[MIT](LICENSE)

## Documentation
[https://nomiden.readthedocs.io](https://nomiden.readthedocs.io)

## Development
This package was built under Python 3.10.8 for Windows 10 and passed the Github Actions: Python package tests under Python 3.8, 3.9, and 3.10 for Ubuntu-latest, MacOS-latest, Windows-latest. To contribute for development, please use [requirements.txt](https://github.com/divakartika/nomiden/blob/main/requirements.txt).

## Getting Help & Discussion

For usage questions and development discussions, feel free to contact diva@algorit.ma.