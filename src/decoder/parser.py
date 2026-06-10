import json

def parse_decoder_output(decoded_output):
    decoded_data = json.loads(decoded_output)
    return decoded_data

def extract_required_fields(decoded_data):

    telemetry = {
        "packet_id":
        decoded_data["beacon_header_packet_id"],

        "timestamp":
            decoded_data["beacon_payload_timestamp"],

        "batt_a_voltage":
            decoded_data["beacon_payload_batt_a_voltage"],

        "batt_b_voltage":
            decoded_data["beacon_payload_batt_b_voltage"],

        "batt_a_current":
            decoded_data["beacon_payload_batt_a_current"],

        "batt_b_current":
            decoded_data["beacon_payload_batt_b_current"],

        "batt_a_temp":
            decoded_data["beacon_payload_batt_a_temp"],

        "batt_b_temp":
            decoded_data["beacon_payload_batt_b_temp"],

        "obc_temp":
            decoded_data["beacon_payload_obc_temp"],

        "power_consumption":
            decoded_data["beacon_payload_power_consumption"],

        "subsystem_status_bitmap":
            decoded_data["beacon_payload_subsystem_status_bitmap"]
    }

    return telemetry
