#!/usr/bin/python3

def class_to_json(obj):
    """Return the dictionary description for JSON serialization of an object."""
    attributes = {}
    
    for attr in dir(obj):
        # Exclude private and built-in attributes
        if not attr.startswith('_'):
            value = getattr(obj, attr)
            # Check if the value is serializable
            if isinstance(value, (list, dict, str, int, bool)):
                attributes[attr] = value
                
    return attributes
