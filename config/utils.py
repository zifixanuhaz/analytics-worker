# utils.py
import logging
import os
import json
import re
from datetime import datetime
from typing import Any, Dict, List

def log_error(message: str) -> None:
    logging.error(message)

def log_info(message: str) -> None:
    logging.info(message)

def log_debug(message: str) -> None:
    logging.debug(message)

def get_current_datetime() -> datetime:
    return datetime.now()

def load_config() -> Dict[str, Any]:
    try:
        with open('config.json', 'r') as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        return {}

def get_environment_variable(var_name: str) -> str:
    return os.environ.get(var_name)

def extract_phone_number(phone_number: str) -> str:
    pattern = r'\d{3}-\d{3}-\d{4}'
    match = re.search(pattern, phone_number)
    if match:
        return match.group()
    return ''

def validate_phone_number(phone_number: str) -> bool:
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    return bool(re.match(pattern, phone_number))