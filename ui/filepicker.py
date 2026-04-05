import tkinter as tk
from tkinter.filedialog import asksaveasfilename

# Create ONE Tk root globally
_root = tk.Tk()
_root.withdraw()
_root.call('wm', 'attributes', '.', '-topmost', True)  # keep dialogs on top

def pick_file_or_folder(filename):
    path = asksaveasfilename(
        initialfile=filename,
        title="Select the network version of this file or choose a folder to save it"
    )
    return path


# Test case
from models.fileobject import FileObject

FILEOBJECT = FileObject(r"c:\DumpStack.log")
print(FILEOBJECT, FILEOBJECT.hash, FILEOBJECT.modified, FILEOBJECT.size, FILEOBJECT.syncpath)

TESTSELECT = pick_file_or_folder(FILEOBJECT.filename)
print(TESTSELECT)

FILEOBJECT.syncpath = TESTSELECT
print(FILEOBJECT, FILEOBJECT.hash, FILEOBJECT.modified, FILEOBJECT.size, FILEOBJECT.syncpath)
