# layout/config.py
import os

# Version number -- dynamically passed for build scripts
current_version = (1, 5, 1, 0)

# Personal Access Token
pat = os.getenv("DST_KEY")  # replaced during build

# False - uses online module | True uses local module for testing
use_local_module = False

#  Log Folder
log_folder = r"C:\Windows\Logs\Software"

# Friendly Version Number -- used within app for display and reference
# Trim trailing zeros for display
trimmed_version = tuple(current_version)
while trimmed_version and trimmed_version[-1] == 0:
    trimmed_version = trimmed_version[:-1]

APP_VERSION_STR = '.'.join(map(str, trimmed_version))
