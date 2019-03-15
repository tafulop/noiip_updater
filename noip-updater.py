import requests
import json
import datetime

# user config
debug_print_flag = True
user_id = "cmFzcGJlcnJ5LnBpZS56ZXJvQGdtYWlsLmNvbQ=="
auth_key = "Qkw0Y2tjQHQ="
hostname = "raspberrypiezero.ddns.net"

# const
noip_url = "http://" + user_id + \
           ":" + auth_key + \
           "@dynupdate.no-ip.com/nic/update?hostname=" + hostname + \
           "&myip=" \
           
def debug_print(msg):
    if debug_print_flag:
        print(str(datetime.datetime.now()) + ": " + msg)

def request_ip():
    debug_print("Requesting pubblic IP...")
    r = requests.post('http://ifconfig.me')
    #debug_print(r.text)      # response as a string
    json_res = json.loads(r.text)
    debug_print("Got public IP: " + json_res["ip"])
    return json_res["ip"]

def update_noip(public_ip):
    debug_print("Trying to update IP to: " + public_ip)
    r = requests.post(noip_url + public_ip)
    debug_print("Response: " + r.text)      # response as a string

# Start
public_ip = request_ip()
update_noip(public_ip)