import os
import re
from datetime import datetime


def create_subfolders(base_path: str, pattern: str, date: datetime = None) -> str:
    """
    Create subfolders based on the pattern
    :param base_path: base/path/to/folder
    :param pattern: folder1/folder2/%Y/%m/%d
    :param date: datetime
    :return: base/path/to/folder/folder1/folder2/2020/01/01
    """
    # Remove any trailing slashes from the base path
    base_path = base_path.rstrip(os.path.sep)

    # Split the pattern into parts based on '/' delimiter
    parts = pattern.split('/')

    # Create subfolders one by one
    current_path = base_path
    for part in parts:

        if is_strftime_style(part) and date is not None:
            # Format the date as per the part
            part = date.strftime(part)

        # Remove any invalid characters from the part
        part = re.sub(r'[^\w\-_.() ]', '', part)

        # Join the current path with the sanitized part
        current_path = os.path.join(current_path, part)

        # Create the subfolder if it doesn't exist
        if not os.path.exists(current_path):
            os.mkdir(current_path)

    return current_path  # Return the path to the folder


def is_strftime_style(string):
    # Define a regular expression pattern for strftime-style format
    strftime_pattern = r"%[a-zA-Z]"

    # Use re.match to check if the string matches the pattern at the beginning
    match = re.match(strftime_pattern, string)

    # If match is not None, it means the string matches the format
    return match is not None
