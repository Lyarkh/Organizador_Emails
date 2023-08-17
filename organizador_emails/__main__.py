
import os
import sys

sys.path.insert(0, os.getcwd())

from organizador_emails.utils.load_config import LoadConfig

configs = LoadConfig()

from main import Main

all_messages = Main.main(configs.get_variables)

import json

with open('results.json', mode='w') as file:
    json.dump(all_messages, file, indent=4)