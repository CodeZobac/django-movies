import yaml


def yaml_coerce(value):
    """
    Coerces a YAML value to its corresponding Python representation.

    Args:
        value: The YAML value to be coerced.

    Returns:
        The Python representation of the YAML value.

    Raises:
        None.

    """
    if isinstance(value, str):
        # yaml.load returns a Python object from the YAML string
        # Converts string dict "{"dummy": value}" to Python dict {"dummy": value}
        # Useful because sometimes we need to stringify settings this way (like in Dockerfiles)
        return yaml.load(f"dummy:{value}", Loader=yaml.SafeLoader)["dummy"]
    return value
