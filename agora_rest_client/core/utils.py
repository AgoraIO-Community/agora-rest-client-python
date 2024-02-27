import json

def to_json(obj):
    """
    Convert object to json
    
    :param obj: object
    :return json
    """
    return json.loads(json.dumps(obj.__dict__))
