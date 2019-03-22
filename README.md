# HouseBot 

A very obnoxious set of web spiders searching for houses to buy

## Linux Installation
Not yet defined

## Windows Installation

In order to manually install Scrapy library on Windows (using pip package manager only), Twisted library must
be installed first.

1. Download the wheel for [Twisted](https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted), 
from Gohlke.  
Make sure you choose the wheel file that matches your architecture (32/64-bit) 
and Python version.
2. create a new virtual environment
    - `python3 -m venv my_venv_name`
3. to activate the virtual environment on Windows, activate script is in the Scripts folder:
    - `\path\to\env\Scripts\activate`
4. In the command prompt change directories to the folder where you
downloaded the wheel file specified in the first step.
5. pip install the Twisted wheel file you downloaded. Example:
    - `pip install Twisted-18.9.0-cp36-cp36m-win32.whl`
6. Install Scrapy:
    - `pip install scrapy`
7. Test the crawler:
    - `scrapy crawl spiderName`  
    Example:
    - `scrapy crawl immobiliare`  
8. Store the scraped data in a JSON file using the following command:
    - `scrapy crawl spiderName -o output.json`
    




### Troubleshoot:
- If you are experiencing the following problem while testing the Scrapy project:  
**_ImportError: No module named win32api._**  
Install pypiwin32 library:  
    - `pip install pypiwin32`
