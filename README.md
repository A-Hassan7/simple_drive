# Google Drive utility functions to upload and download files

## What is this?

These are utility functions built on top of PyDrive that will allow you to download and upload files to your google drive with minimal lines of code.

## Why is it needed?

The Google Drive API provides a somewhat long-winded process to upload and download files for me. PyDrive makes this process much simpler. These functions make it even simpler.

## Pre-requisite 

1. Install PyDrive: `pip install pydrive`

2. Create Google Drive OAuth credentials
   * Navigate to [PyDrive documentation](https://pythonhosted.org/PyDrive/quickstart.html) and follow the Quickstart authentication instruction. Make sure to **put the client_secrets.json file in your working directory**


## Usage

```python

from simple_drive import Google_drive
drive = Google_drive() # initialize class
drive.authenticate() # follow authentication instructions

#Upload a file
drive.upload('file')

#Download a file
drive.download('file')

#Get a list of files in your drive
drive.list_files()
```
