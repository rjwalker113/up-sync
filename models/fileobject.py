# # fileobject.py

# import os
# import hashlib
# from pathlib import Path
# from datetime import datetime


# class FileObject:
#     '''An object to store basic details for an existing file.'''
#     def __init__(self, path):
#         self.path = Path(path)

#     @property
#     def filename(self):
#         '''Stores Filename without path'''
#         return self.path.name

#     @property
#     def modified(self):
#         '''Stores Date Modified'''
#         return datetime.fromtimestamp(self.path.stat().st_mtime)

#     @property
#     def size(self):
#         '''Stores file size.'''
#         return self.path.stat().st_size
    
#     @property
#     def hash(self, block_size=65536):
#         '''Compute basic hash.'''
#         hasher = hashlib.md5()
#         with open(self.path, "rb") as f:
#             for chunk in iter(lambda: f.read(block_size), b""):
#                 hasher.update(chunk)
#         return hasher.hexdigest()
    
#     @property
#     def syncpath(self):
#         return None

#     def _syncpath(self):
#         pass

#     def __str__(self): 
#         return f"{self.path})"
    
#     def __repr__(self): 
#         return f"{self.path!r})"

import hashlib
from pathlib import Path
from datetime import datetime

class FileObject:
    '''An object to store basic details for an existing file.'''
    def __init__(self, path):
        self.path = Path(path)
        self._syncpath = None

    @property
    def filename(self):
        return self.path.name

    @property
    def modified(self):
        return datetime.fromtimestamp(self.path.stat().st_mtime)

    @property
    def size(self):
        return self.path.stat().st_size
    
    @property
    def hash(self):
        return self._compute_hash()

    def _compute_hash(self, block_size=65536):
        hasher = hashlib.md5()
        with open(self.path, "rb") as f:
            for chunk in iter(lambda: f.read(block_size), b""):
                hasher.update(chunk)
        return hasher.hexdigest()

    @property
    def syncpath(self):
        return self._syncpath

    @syncpath.setter
    def syncpath(self, value):
        self._syncpath = value

    def __str__(self):
        return str(self.path)
    
    def __repr__(self):
        return f"FileObject({self.path!r})"
