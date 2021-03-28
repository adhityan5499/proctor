import subprocess
import json
output = subprocess.Popen(["python", "audio_save_required_audios_only.py"], shell=True, stdout=subprocess.PIPE)
jsonS, _ = output.communicate()
data = json.loads(jsonS)
print(data)
