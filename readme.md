# Main deployment repository of machine and me

[![Deliver](https://github.com/machineandme/machineand.me/workflows/Deliver/badge.svg)](https://github.com/machineandme/machineand.me/actions)


![](http://machineand.me/m1.png)


## Content

Any subproject stored at [`./data/`](https://github.com/machineandme/machineand.me/tree/master/data):

+ Folder [`./data/server`](https://github.com/machineandme/machineand.me/tree/master/data/server) is static files, like HTML and CSS, for website [machineand.me](https://machineand.me)
+ Submodule `./data/shirts/` is link to [github.com/machineandme/shirts](https://github.com/machineandme/shirts)
+ Submodule `./data/ticker/` is link to [github.com/machineandme/ticker-backend](https://github.com/machineandme/ticker-backend)

## Ansible

### About ansible

+ Ansible configuration file [`./ansible.cfg`](https://github.com/machineandme/machineand.me/tree/master/ansible.cfg)  
    [Ansible config simple info](https://docs.ansible.com/ansible/2.9/installation_guide/intro_configuration.html#configuration-file)
+ Ansible inventory is list of server used for deploy  
    [Ansible inventory simple info](https://docs.ansible.com/ansible/2.9/network/getting_started/first_inventory.html)
+ We use [`./build_inventory.py`](https://github.com/machineandme/machineand.me/tree/master/build_inventory.py) to dynamically create inventory from Digital Ocean droplets list

### About playbooks

+ Playbooks is CI/CD steps [`./playbooks/`](https://github.com/machineandme/machineand.me/tree/master/playbooks)  
    [Ansible playbook simple info](https://docs.ansible.com/ansible/2.9/user_guide/playbooks.html)
+ Datadog playbook installs and setup datadog agents on servers [`./playbooks/datadog.yaml`](https://github.com/machineandme/machineand.me/tree/master/playbooks/datadog.yaml)

### More about playbooks

Playbooks divided by host type:
```bash
./playbooks/${host_type}
```
And by task name
```bash
./playbooks/${host_type}/${task_name}.yaml
```
| file | desc |
|---|---|
|[`./playbooks/cache/redis.yaml`](https://github.com/machineandme/machineand.me/blob/master/playbooks/cache/redis.yaml) | instruction to run [Redis](http://redis.io) server |
|[`./playbooks/machines/upload.yaml`](https://github.com/machineandme/machineand.me/tree/master/playbooks/machines/upload.yaml) | instruction for upload static, configs and app data to target server|
|[`./playbooks/machines/caddy.yaml`](https://github.com/machineandme/machineand.me/tree/master/playbooks/machines/caddy.yaml) | instruction to copy [`Caddyfile`](https://github.com/machineandme/machineand.me/blob/master/data/server/Caddyfile) and setup [Caddy](http://caddyserver.com) as server|
|[`./playbooks/machines/shirts.yaml`](https://github.com/machineandme/machineand.me/tree/master/playbooks/machines/shirts.yaml) | instruction for delivering [machineandme/shirts](https://github.com/machineandme/shirts)|
|[`./playbooks/machines/ticker.yaml`](https://github.com/machineandme/machineand.me/tree/master/playbooks/machines/ticker.yaml) |  instruction for delivering [machineandme/ticker-backend](https://github.com/machineandme/ticker-backend)|