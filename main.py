import json
import os
import datetime

import imapclient
import pyzmail as pyzmail
import shutil
from ftputil import FTPHost


# TRY Load configuration from config.json:
try:
    with open('config.json') as f:
        config = json.load(f)
except FileNotFoundError:
    print('Configuration file not found.')
    exit(1)

# Define the path to the folder where you want to save the attachment
save_folder = './files'

# Ensure the folder exists; create it if it doesn't
if not os.path.exists(save_folder):
    os.makedirs(save_folder)


# Connect to the Email Server:
imap_server = imapclient.IMAPClient(host=config['email']['host'],
                                    port=config['email']['port'],
                                    ssl=config['email']['ssl'] or False)
imap_server.login(username=config['email']['username'], password=config['email']['password'])

# Select the Mailbox and Search for Emails:
imap_server.select_folder(folder=config['email']['folder'], readonly=True)

if (config['preferences']['moveEmailToFolder']
        and not imap_server.folder_exists(folder=config['preferences']['moveEmailToFolderName'])):
    imap_server.create_folder(folder=config['preferences']['moveEmailToFolderName'])

for msg_filer in config['email']['filters']:
    criteria = []
    for key, value in msg_filer.items():
        key = key.upper()
        if key == 'UNSEEN' and value:
            criteria.append(key)
        elif key == 'UNSEEN' and not value:
            continue
        else:
            criteria.append(key)
            criteria.append(value)

    messages = imap_server.search(criteria)

    # Download Attachments and Move Email:
    for msg_id, message_data in imap_server.fetch(messages[:2], 'RFC822').items():
        email_message = pyzmail.PyzMessage.factory(message_data[b'RFC822'])
        for part in email_message.mailparts:
            if part.filename is not None:
                # Construct the full path for saving the attachment
                save_path = os.path.join(save_folder, part.filename)

                # Save the attachment to the specified folder
                with open(save_path, 'wb') as f:
                    f.write(part.get_payload())

        # Move the email to another folder (e.g., "Processed")
        if config['preferences']['moveEmailToFolder']:
            imap_server.move([msg_id], config['preferences']['moveEmailToFolderName'])

        # shutil.move('Your Attachment Name Here', 'Your Destination Here')

        # Delete Email:
        # imap_server.delete_messages(msg_id)
        # imap_server.expunge()

# Disconnect from the Email Server:
imap_server.logout()

FTP_HOST = config['ftp']['host']
FTP_USER = config['ftp']['username']
FTP_PASS = config['ftp']['password']

# Connect to the FTP Server:
with FTPHost(FTP_HOST, FTP_USER, FTP_PASS) as ftp_host:
    print(ftp_host.getcwd())
    # Create a directory for the 'ftpUploadFolder' if it doesn't exist
    if not ftp_host.path.exists(config['preferences']['ftpUploadFolder']):
        ftp_host.mkdir(config['preferences']['ftpUploadFolder'])

    # Change to the 'ftpUploadFolder' directory
    ftp_host.chdir(config['preferences']['ftpUploadFolder'])
    print(ftp_host.getcwd())
    # Get a list of files in the 'save_folder' directory
    files = os.listdir(save_folder)
    for file in files:
        # "Invoice 2045195266 11.09.2023" from filename get year and month
        # year = file.split(' ')[-1].split('.')[2]
        # month = file.split(' ')[-1].split('.')[1]
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
        ftp_host.chdir(config['preferences']['ftpUploadFolder'])

        # Delete the file from the local folder
        os.remove(local_path)


print('Done!')
