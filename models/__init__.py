#!/usr/bin/python3
"""The initializer of my package"""
from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()
