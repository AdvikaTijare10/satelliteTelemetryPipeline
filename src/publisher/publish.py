import json
def publish_to_mqtt(client,telemetry):
    payload=json.dumps(telemetry) #converts the python dict to json format for input to mqtt
    
    result=client.publish("satellite/telemetry",payload)
    result.wait_for_publish()
   
