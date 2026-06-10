import subprocess
import tempfile
def create_temp_file(raw_frame):    
   
        binary_data=bytes.fromhex(raw_frame)       
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(binary_data)
            temp_path = temp_file.name
        return temp_path  
        

def decode_frame(temp_path):

    result = subprocess.run(
        ["decode_frame", "uwe4", temp_path],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return None

    return result.stdout