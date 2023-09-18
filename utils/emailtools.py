import os

import pyzmail
from imapclient import imapclient

from utils.config import EmailConfig


class EmailTools:
    """
    EmailTools class

    """
    def __init__(self, email_config: EmailConfig):
        self.host = email_config.host
        self.port = email_config.port
        self.ssl = email_config.ssl
        self.username = email_config.username
        self.password = email_config.password
        self.folder = email_config.folder
        self.imap_server = None

    def connect(self):
        """
        Connect to the Email Server

        """
        imap_server = imapclient.IMAPClient(host=self.host,
                                            port=self.port,
                                            ssl=self.ssl)
        imap_server.login(username=self.username, password=self.password)
        self.imap_server = imap_server

    def disconnect(self):
        """
        Disconnect from the Email Server

        """
        self.imap_server.logout()

    def select_folder(self, folder=None, readonly=True):
        """
        Select the Mailbox and Search for Emails

        """
        if folder is None:
            folder = self.folder
        self.imap_server.select_folder(folder=folder, readonly=readonly)

    @staticmethod
    def get_criteria(msg_filer):
        """
        Get the criteria for the search

        """
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
        return criteria

    def search(self, criteria):
        """
        Search for emails

        """
        messages = self.imap_server.search(criteria)
        return messages

    def download_attachments(self, message_id, save_folder):
        """
        Download Attachments and Move Email

        """
        for _, message_data in self.imap_server.fetch(message_id, 'RFC822').items():
            email_message = pyzmail.PyzMessage.factory(message_data[b'RFC822'])
            for part in email_message.mailparts:
                if part.filename is not None:
                    # Construct the full path for saving the attachment
                    save_path = os.path.join(save_folder, part.filename)

                    # Save the attachment to the specified folder
                    with open(save_path, 'wb') as f:
                        f.write(part.get_payload())

    def move_email(self, message_id, folder):
        """
        Move the email to another folder (e.g., "Processed")

        """
        if not self.imap_server.folder_exists(folder=folder):
            self.imap_server.create_folder(folder=folder)

        self.imap_server.move([message_id], folder)

    def get_message_date(self, message_id):
        """
        Get the date of the email

        """
        data = self.imap_server.fetch(message_id, ['INTERNALDATE'])
        return data[message_id][b'INTERNALDATE']

