#!/usr/bin/python3
"""
This creates a unique filestorage instance for my application
"""


from engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
