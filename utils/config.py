# TRY Load configuration from config.json:
import json

try:
    with open('config.json') as f:
        config = json.load(f)
except FileNotFoundError:
    print('Configuration file not found.')
    exit(1)


class EmailConfig:
    host = config['email']['host']
    port = config['email']['port']
    ssl = config['email']['ssl'] or False
    username = config['email']['username']
    password = config['email']['password']
    folder = config['email']['folder']


class EmailTask:
    tasks = config['email']['tasks']


class FtpConfig:
    host = config['ftp']['host']
    port = config['ftp']['port']
    username = config['ftp']['username']
    password = config['ftp']['password']
    uploadFolder = config['ftp']['uploadFolder']


class PreferencesConfig:
    moveEmailToFolder = config['preferences']['moveEmailToFolder']
    moveEmailToFolderName = config['preferences']['moveEmailToFolderName']
    deleteEmail = config['preferences']['deleteEmail']


class Config:
    email = EmailConfig
    ftp = FtpConfig
    preferences = PreferencesConfig
