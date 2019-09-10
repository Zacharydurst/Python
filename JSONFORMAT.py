import subprocess
import os
import re
import json


# Find the data, grab shizz
commands = 'cd sdcard/pos/\nls -la\nexit\n'

value1 = subprocess.Popen((['adb', 'shell']), stdin = subprocess.PIPE, stdout= subprocess.PIPE)
out, err = value1.communicate(commands.encode('utf-8'))

out_decode = out.decode("utf-8")

finds = re.findall(r'([0-9]+\.json)', out_decode)


# From here, collect the most recent data and output it.
commands = 'cd sdcard/pos/\ncat ' + finds[-1] + '\nexit\n'

value1 = subprocess.Popen((['adb', 'shell']), stdin = subprocess.PIPE, stdout= subprocess.PIPE)
out, err = value1.communicate(commands.encode('utf-8'))

out_decode = out.decode("utf-8")
#print(out_decode)

#JSON Formatting
result = out_decode.replace('\r', '')
result = result.replace('\n', '')
result = result.replace('\\\"','\"')
result = result.replace("shell@P027:/sdcard/pos $ exit", "")
result = result.replace('payload":\"', 'payload\":')
result = result.replace('","platform"', ',"platform"')
result = result[result.find('{'):]
resultJson = json.loads(result)
result = json.dumps(resultJson, indent=4, sort_keys=True)
print(result)



    




