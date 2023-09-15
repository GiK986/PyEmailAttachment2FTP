# PyEmailAttachment2FTP

PyEmailAttachment2FTP is a Python script that simplifies the task of downloading email attachments and transferring them directly to an FTP server. This script streamlines the process, making it ideal for automating tasks like backup, file sharing, and data processing.

## Features

- Automatically fetches email attachments.
- Uploads attachments to a specified FTP server.
- Customizable and easy-to-use configuration.
- Compatible with various email providers and FTP servers.

## Requirements

- Python 3.x
- Required Python libraries: imapclient, pyzmail, ftputil

## Getting Started

1. Clone this repository to your local machine.

   ```shell
   git clone https://github.com/yourusername/PyEmailAttachment2FTP.git
   cd PyEmailAttachment2FTP
    ```
   
2. Install the required Python libraries.

   ```shell
   pip install -r requirements.txt
   ```

3. Configure the script by editing the `config.json` file and edit the configuration settings.  
Provide your email and FTP server details, customize filters, and set up your preferences.

    ```json
   {
     "email": {
       "host": "imap.example.com",
       "port": 993,
       "username": "your_email@example.com",
       "password": "your_email_password",
       "ssl": true,
       "folder": "inbox",
       "filters": [
         {
           "subject": "Important Report",
           "from": "report@example.com",
           "hasAttachment": true
         }
       ]
     },
     "ftp": {
       "host": "ftp.example.com",
       "port": 21,
       "username": "your_ftp_username",
       "password": "your_ftp_password",
       "folder": "uploads",
       "ssl": false,
       "passive": true,
       "timeout": 30,
       "retries": 3,
       "retryDelay": 5
     },
     "preferences": {
       "deleteEmail": false,
       "deleteEmailDelay": 0,
       "deleteEmailDelayUnit": "minutes",
       "moveEmailToFolder": false,
       "moveEmailToFolderName": "archived"
     }
   }
    ```

4. Run the script.

   ```shell
   python main.py
   ```

5. (Optional) Schedule the script to run automatically.

   ```shell
   python scheduler.py
   ```
    > **Note:** The scheduler script is only available for Windows. If you are using Linux, you can use the `cron` utility to schedule the script.

## Configuration

The `config.json` file contains the configuration settings for the script. The following table describes the configuration settings.

| Setting                             | Description                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| `email`                             | Email configuration settings.                                                                   |
| `email.host`                        | The IMAP server address of your email provider.                                                 |
| `email.port`                        | The IMAP server port of your email provider.                                                    |
| `email.username`                    | Your email address.                                                                             |
| `email.password`                    | Your email password.                                                                            |
| `email.ssl`                         | Set to `true` if your email provider uses SSL.                                                  |
| `email.folder`                      | The folder where the script will look for email attachments.                                    |
| `email.filters`                     | The filters that the script will use to find email attachments.                                 |
| `email.filters[].subject`           | The subject of the email.                                                                       |
| `email.filters[].from`              | The sender of the email.                                                                        |
| `email.filters[].to`                | The recipient of the email.                                                                     |
| `email.filters[].hasAttachment`     | Set to `true` if the email has an attachment.                                                   |
| `ftp`                               | FTP configuration settings.                                                                     |
| `ftp.host`                          | The FTP server address.                                                                         |
| `ftp.port`                          | The FTP server port.                                                                            |
| `ftp.username`                      | Your FTP username.                                                                              |
| `ftp.password`                      | Your FTP password.                                                                              |
| `ftp.folder`                        | The folder where the script will upload the email attachments.                                  |
| `ftp.ssl`                           | Set to `true` if your FTP server uses SSL.                                                      |
| `ftp.passive`                       | Set to `true` if your FTP server uses passive mode.                                             |
| `ftp.timeout`                       | The timeout of the FTP connection.                                                              |
| `ftp.retries`                       | The number of times the script will retry to connect to the FTP server.                         |
| `ftp.retryDelay`                    | The delay between each retry.                                                                   |
| `preferences`                       | Script preferences.                                                                             |
| `preferences.deleteEmail`           | Set to `true` if you want to delete the email after downloading the attachment.                 |
| `preferences.deleteEmailDelay`      | The delay before deleting the email.                                                            |
| `preferences.deleteEmailDelayUnit`  | The unit of the delay before deleting the email.                                                |
| `preferences.moveEmailToFolder`     | Set to `true` if you want to move the email to another folder after downloading the attachment. |
| `preferences.moveEmailToFolderName` | The name of the folder where the script will move the email.                                    |

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [imapclient](https://github.com/mjs/imapclient)
- [pyzmail](https://github.com/aspineux/pyzmail)
- [ftputil](https://github.com/smurfix/ftputil)

## Contact

If you have any questions or concerns, you can reach me at [g.kyosev86@gmail.com](mailto:g.kyosev86@gmail.com).

Happy coding!
