import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("api_key")

URL = "https://db.satnogs.org/api/telemetry/"
SATELLITE_ID = "43880"

MQTT_HOST = "localhost"
MQTT_PORT = 1883

