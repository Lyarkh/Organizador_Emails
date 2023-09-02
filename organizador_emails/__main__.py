import os
import sys

sys.path.insert(0, os.getcwd())

from organizador_emails.utils.load_config import LoadConfig
from organizador_emails.google_api.gmail.functions.get_messages import (
    Getmessages,
)
from organizador_emails.google_api.service_interface import ServiceInterface

configs = LoadConfig()

from main import Main

all_messages = Main.main(configs.get_variables)

import json

with open('results.json', mode='w') as file:
    json.dump(all_messages, file, indent=4)
