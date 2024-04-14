from core.core.utils.collections import deep_update
from core.core.utils.settings import get_settings_from_envirmoment

"""
This takes env variables with a matching prefix, strips out the prefix and adds it to global

For example:
export CORESETTING_IN_DOCKER=True (enviroment variable)

Could then be referenced as a global as
IN_DOCKER (where the value would be True)
"""

# globals() is a dictionary of global variables in the current module

deep_update(globals(), get_settings_from_envirmoment(ENVVAR_SETTINGS_PREFIX))
