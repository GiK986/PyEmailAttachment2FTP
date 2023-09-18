import os

from utils.config import EmailConfig, EmailTask
from utils.emailtools import EmailTools
from utils.helpers import create_subfolders


def main():
    # Define the path to the folder where you want to save the attachment
    save_folder = './files'

    # Ensure the folder exists; create it if it doesn't
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    email_config = EmailConfig()

    # Connect to the Email Server:
    email_server = EmailTools(email_config)
    email_server.connect()

    tasks = EmailTask().tasks

    for task in tasks:
        # Select the Mailbox and Search for Emails:
        search_folder = task['searchFolder']
        readonly = task['readonly']
        email_server.select_folder(search_folder, readonly)

        criteria = email_server.get_criteria(task['searchCriteria'])
        messages = email_server.imap_server.search(criteria)

        move_email_to_folder_name = task['moveEmailToFolderName']

        # Download Attachments and Move Email:
        for msg_id in messages:

            save_folder = create_subfolders(task['saveRootFolder'], task['saveSubFolderPattern'], email_server.get_message_date(msg_id))
            email_server.download_attachments(msg_id, save_folder)
            email_server.move_email(msg_id, move_email_to_folder_name)

    # Disconnect from the Email Server:
    email_server.disconnect()

    print('Done!')


if __name__ == '__main__':
    main()
