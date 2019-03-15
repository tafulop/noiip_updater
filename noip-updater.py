import requests
import json
import datetime

# user config
debug_print_flag = True
user_id = "" # base64 encoded username
auth_key = "" # base64 encoded password
hostname = "" # name of the DDNS host (eg. raspberrypiezeero.ddns.net)
headers = {'user-agent': 'noip-updater on Raspbian/1.0.0 tamas.flp@gmail.com'}

# const
noip_url = "https://" + user_id + \
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
    r = requests.post(noip_url + public_ip, headers=headers)
    #debug_print("Request string:\n" + noip_url + public_ip)
    debug_print("Response: " + r.text)      # response as a string

# Start
public_ip = request_ip()
update_noip(public_ip)
