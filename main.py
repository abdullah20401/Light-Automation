from tuya_connector import TuyaOpenAPI
import json

secrets = json.load(open('secret.json', 'r'))

ACCESS_ID = secrets['access_id']
ACCESS_KEY = secrets['access_key']

ENDPOINT = secrets['endpoint']

USERNAME = secrets['username']
PASSWORD = secrets['password']

LIGHTBULB_DEVICE_ID = secrets['lightbulb_device_id']

openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()

commands = {
    'commands': [
        {
            'code': 'temp_value_v2',
            'value': 1000
        }
    ]
}

result = openapi.post(f'/v1.0/iot-03/devices/{LIGHTBULB_DEVICE_ID}/commands', commands)
# result = openapi.get(f'/v1.0/iot-03/devices/{LIGHTBULB_DEVICE_ID}/status') # Gets the status of the bulb

print(result)
