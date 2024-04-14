import os
from .misc import yaml_coerce


def get_settings_from_envirmoment(prefix):
    """
    Retrieves settings from the environment variables based on a given prefix.

    Args:
        prefix (str): The prefix used to filter the environment variables.

    Returns:
        dict: A dictionary containing the settings retrieved from the environment variables.
    """
    prefix_len = len(prefix)
    return {key[prefix_len:]: yaml_coerce(value) for key, value in os.environ.items() if key.startswith(prefix)}

    
