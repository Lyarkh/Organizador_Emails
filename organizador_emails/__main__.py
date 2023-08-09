
import os
import sys

sys.path.insert(0, os.getcwd())

from organizador_emails.utils.load_config import LoadConfig

LoadConfig()

from main import Main

Main.main()
