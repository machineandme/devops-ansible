import requests
import yaml
import os


headers = {
    "Authorization": "Bearer %s" % os.getenv("DO_API_KEY")
}

r = requests.get("https://api.digitalocean.com/v2/droplets",
                 headers=headers)
r.raise_for_status()

inventory = dict()

for droplet in r.json()['droplets']:
    ips = [n['ip_address']
           for n in droplet['networks']['v4']
           if n['type'] == 'public']
    for tag in droplet['tags']:
        inventory.setdefault(tag, dict(hosts=dict()))
        inventory[tag]['hosts'][droplet['name']] = {
            "ansible_host": ips[0]
        }

with open('inventory.yaml', 'w') as file:
    file.write(yaml.safe_dump(inventory))

