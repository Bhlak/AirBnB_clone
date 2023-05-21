#!/usr/bin/python3
"""Initiates an instance of FileSorage"""
from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
