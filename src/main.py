import paho.mqtt.client as mqtt
import os
import time

from src.satnogs.data_fetch import get_frames_from_satNGOS
from src.decoder.frame_decoder import create_temp_file,decode_frame
from src.decoder.parser import parse_decoder_output,extract_required_fields
from src.publisher.publish import publish_to_mqtt

frames = get_frames_from_satNGOS()
print("Total frames fetched:", len(frames))
success_count=0
failed_count=0
client=mqtt.Client()
client.connect("localhost",1883)

for frame in frames:
    
    try:
        timestamp=frame['timestamp']
        raw_frame=frame['frame']

        temp_path=create_temp_file(raw_frame)

        decoded_output=decode_frame(temp_path)
        os.remove(temp_path)

        if decoded_output is None:
                failed_count+=1
                continue

        decoded_data=parse_decoder_output(decoded_output)
        telemetry=extract_required_fields(decoded_data)
        print(telemetry)
        publish_to_mqtt(client,telemetry)
        success_count+=1
        time.sleep(2)
        
        print(f"Frame {success_count} ")
        
    except Exception as e:
        failed_count+=1
        print(f"Frame {failed_count} ")
        print("Frame decoding failed ",e)
client.disconnect()
print("Success:", success_count)
print("Failed:", failed_count)


