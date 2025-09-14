#!/usr/bin/python3
"Initialize the models packages"

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
