# Connect to the FTP Server:
import datetime
import os

from ftputil import FTPHost

from utils.config import Config

ftp = Config.ftp

save_folder = './files'

with FTPHost(ftp.host, ftp.username, ftp.password) as ftp_host:
    print(ftp_host.getcwd())
    # Create a directory for the 'ftpUploadFolder' if it doesn't exist
    if not ftp_host.path.exists(ftp.uploadFolder):
        ftp_host.mkdir(ftp.uploadFolder)

    # Change to the 'ftpUploadFolder' directory
    ftp_host.chdir(ftp.uploadFolder)
    print(ftp_host.getcwd())
    # Get a list of files in the 'save_folder' directory
    files = os.listdir(save_folder)
    for file in files:
        # from string to datetime
        date = datetime.datetime.strptime(file.split(' ')[-1][:10], '%d.%m.%Y')
        year = str(date.year)
        month = date.strftime('%B')
        # Create a directory for the year if it doesn't exist
        if not ftp_host.path.exists(year):
            ftp_host.mkdir(year)
        # Change to the year directory
        ftp_host.chdir(year)
        # Create a directory for the month if it doesn't exist
        if not ftp_host.path.exists(month):
            ftp_host.mkdir(month)
        # Change to the month directory
        ftp_host.chdir(month)

        # Construct the full local path
        local_path = os.path.join(save_folder, file)

        # Upload the file to the FTP server
        ftp_host.upload(local_path, file)

        # Change to the 'ftpUploadFolder' directory
        ftp_host.chdir(ftp.uploadFolder)

        # Delete the file from the local folder
        os.remove(local_path)

