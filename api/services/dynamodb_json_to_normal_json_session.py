from boto3.dynamodb.types import TypeDeserializer
from typing import Dict

def dynamodb_json_to_normal_json(dynamodb_json: Dict) -> Dict:
    """Convert DynamoDB JSON to standard JSON."""
    deserializer = TypeDeserializer()
    return {key: deserializer.deserialize(value) for key, value in dynamodb_json.items()}
