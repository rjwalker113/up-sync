# layout/utils.py

import sys, os, tempfile, shutil

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller """
    try:
        base_path = sys._MEIPASS  # Only exists in PyInstaller
    except AttributeError:
        base_path = os.path.abspath(".")  # Use local path when running normally
    return os.path.join(base_path, relative_path)

def cleanup(foldername_or_path, in_temp=True):
    if in_temp:
        temp_path = tempfile.gettempdir()
        full_path = os.path.join(temp_path, foldername_or_path)
    else:
        full_path = foldername_or_path

    if not os.path.isdir(full_path):
        print(f"\033[93mFoder not found: {foldername_or_path}\033[0m")
        return False
    else:
        try:
            shutil.rmtree(full_path)
            print(f"\033[93mDeleted folder: {foldername_or_path}\033[0m")
            return True
        except Exception as e:
            print(f"\033[91mDelete Failed: {full_path}: {e}\033[0m")
            return False
