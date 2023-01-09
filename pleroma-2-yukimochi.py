#!/usr/bin/python3

import json

new_data = dict()
new_data["RedisClient"] = dict()
new_data["relayConfig"] = dict()
new_data["subscriptions"] = list()
subs = new_data["subscriptions"]

with open('relay.jsonld', 'r') as f:
    data = json.load(f)

    for i in data["relay-list"]:
        cur_data = data["relay-list"][i]

        subs.append(dict())
        subs[-1]["domain"] = cur_data["domain"]
        subs[-1]["inbox_url"] = cur_data["inbox"]
        subs[-1]["activity_id"] = cur_data["followid"]
        subs[-1]["actor_id"] = cur_data["inbox"].replace("/inbox", "/actor")

    with open('new-yuki.json', 'w') as f2:
        f2.write(json.dumps(new_data))