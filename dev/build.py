import os
import subprocess
from layout.config import APP_VERSION_STR

# To run this file properly in console:
# python -m dev.build

# --- CONFIG ---
build_number = APP_VERSION_STR
exe_name = f"DevOps-Support-Toolkit-v{build_number}"
target_file = "layout/config.py"
insert_line = 8  # Line number to insert the PAT
pat = os.getenv("DST_KEY")
if not pat:
    raise ValueError("Environment variable DST_KEY not found.")

line_to_insert = f'pat = "{pat}"\n'
line_to_revert = f'pat = os.getenv("DST_KEY")  # replaced during build\n'

# --- READ ORIGINAL FILE ---
with open(target_file, "r") as f:
    lines = f.readlines()

# --- INJECT PAT ---
lines[insert_line - 1] = line_to_insert
with open(target_file, "w") as f:
    f.writelines(lines)

print(f"Injected PAT into {target_file} at line {insert_line}")

# --- EXPORT CURRENT VERSION INFO
result = subprocess.run(
    ["python", "-m", "update.set_version_details"],
    capture_output=True,
    text=True
)

print("STDOUT:\n", result.stdout)
print("STDERR:\n", result.stderr)


# --- BUILD STEP ---
pyinstaller_cmd = [
    "pyinstaller",
    "main.py",
    f"--name={exe_name}",
    "--icon=images/FieldOps_AppIcon_256.ico",
    "--onefile",
    "--windowed",
    "--uac-admin",
    "--clean",
    "--add-data=images:images",
    "--add-data=fonts:fonts",
    "--version-file=update/version.txt"
]

print("Building with PyInstaller...")
subprocess.run(pyinstaller_cmd, check=True)
print("Build complete")

# --- REMOVE INJECTED LINE ---
lines[insert_line - 1] = line_to_revert
with open(target_file, "w") as f:
    f.writelines(lines)

print(f"Removed injected PAT from {target_file}")