''' This module allows the user to create a PyDrive GoogleDrive instence and read or write to thier google drive '''


from pydrive.auth import GoogleAuth as ga
from pydrive.drive import GoogleDrive as gd


class Google_drive():
    def __init__(self):
        pass

    def authenticate(self):
        '''returns authenticated google drive object'''

        gauth = ga()
        gauth.LocalWebserverAuth()
        self.drive = gd(gauth)


    def download(self, filename):
        '''downloads specified file from google drive to working directory'''

        # getting list of files from google drive
        file_list = self.drive.ListFile(
            {'q': "'root' in parents and trashed=false"}).GetList()

        # searching through the list of files to find filename and grabing ID
        for file in file_list:
            if file['title'] == filename:
                fileID = file['id']

        # downloading file to current directory
        file1 = self.drive.CreateFile({'id': fileID})
        file1.GetContentFile(filename)
        print(f'{filename} successfully downloaded to current directory')


    def upload(self, file):
        '''upload specified file to google drive'''

        file1 = self.drive.CreateFile({'title': f'{file}'})
        file1.SetContentFile(file1['title'])
        file1.Upload()
        print(f'{file} successfully uploaded to google drive')


    def list_files(self):
        '''returns a list files within google drive'''

        file_names = []
        file_list = self.drive.ListFile(
            {'q': "'root' in parents and trashed=false"}).GetList()
        for file in file_list:
            file_names.append(file['title'])
        return file_names
