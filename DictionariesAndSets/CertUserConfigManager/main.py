def add_setting(settings, setting):
    key, value = setting
    key = key.lower()
    value = value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
        
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings, setting):
    key, value = setting
    key = key.lower()
    value = value.lower()
