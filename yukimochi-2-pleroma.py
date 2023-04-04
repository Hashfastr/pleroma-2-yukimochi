#!/usr/bin/python3

# Pleroma
#"relay-list": {
#        "eozygodon.com": {
#            "domain": "eozygodon.com",
#            "inbox": "https://eozygodon.com/inbox",
#            "followid": "https://eozygodon.com/4dc0e1d2-cc85-4271-94c2-e96ae2420fc6",
#            "software": "mastodon"
#        },

# Yuki
# {
#   "domain":"publicsquare.global",
#   "inbox_url":"https://publicsquare.global/inbox",
#   "activity_id":"https://publicsquare.global/63a83b79-22bd-44de-b1c0-bf88fc82285f",
#   "actor_id":"https://publicsquare.global/actor"
# }

import json

new_data = dict()
new_data['relay-list'] = dict()
subs = new_data['relay-list']

with open('backup.json', 'r') as f:
    data = json.load(f)

    for i in data["subscriptions"]:
        subs[i['domain']] = dict()
        subs[i['domain']]['domain'] = i['domain']
        subs[i['domain']]['inbox'] = i['inbox_url']
        subs[i['domain']]['followid'] = i['activity_id']
        subs[i['domain']]['software'] = "unknown"

    new_data['private-key'] = ''
    new_data['follow-requests'] = dict()
    new_data['version'] = 1
    with open('actor.pem', 'r') as key:
        for line in key:
            new_data['private-key'] = new_data['private-key'] + line

    with open('new-pleroma.jsonld', 'w') as f2:
        f2.write(json.dumps(new_data, indent=4))
