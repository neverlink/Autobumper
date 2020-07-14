import requests
import json
import time
from datetime import datetime

with open('config.json', 'rb') as file:
    json_data = json.load(file)

cookie = json_data["cookie"]
my_post_key = json_data["my_post_key"]
signature = json_data["signature"]
thread_queue = json_data["thread_queue"]
bump_delay = json_data["bump_delay"]
proxies = json_data["proxies"]

params = {'ajax': 1}
headers = {'cookie': cookie, 'content-type': 'application/x-www-form-urlencoded'}

def bump_threads():
    for thread_id, message in thread_queue.items():
        body = f'my_post_key={my_post_key}&action=do_newreply&tid={thread_id}&method=quickreply&message={message}&postoptions%5Bsignature%5D={signature}'
        try:
            json_response = requests.post('https://ogusers.com/newreply.php', params=params, headers=headers, data=body, proxies=proxies).json()
            current_time = datetime.now().strftime('%H:%M:%S')

            if "data" in json_response:
                print(f'[{current_time}] Bumped thread {thread_id} - {message}')
            else:
                print(f'[{current_time}] Failed to bump {thread_id} - {json_response["errors"]}')
            time.sleep(bump_delay["posts"])
        except:
            print("Update your proxies and try again!")
            quit()

while True:
    bump_threads()
    current_time = datetime.now().strftime('%H:%M:%S')
    print(f'[{current_time}] Waiting for next batch')
    time.sleep(bump_delay["threads"])