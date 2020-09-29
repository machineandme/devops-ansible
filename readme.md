# Main deployment repository of machine and me

[![Deliver](https://github.com/machineandme/machineand.me/workflows/Deliver/badge.svg)](https://github.com/machineandme/machineand.me/actions)


![](http://machineand.me/m1.png)


## Content

Any submodule stored at [`./data/`](https://github.com/machineandme/machineand.me/tree/master/data):

+ Folder [`./data/server`](https://github.com/machineandme/machineand.me/tree/master/data/server) is static files, like HTML and CSS, for website [machineand.me](https://machineand.me)
+ Submodules

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
|[`./playbooks/machines/codetee.yaml`](https://github.com/machineandme/machineand.me/tree/master/playbooks/machines/codetee.yaml) | instruction for delivering [machineandme/codetee-backend-python](https://github.com/machineandme/codetee-backend-python)|
|[`./playbooks/machines/ticker.yaml`](https://github.com/machineandme/machineand.me/tree/master/playbooks/machines/ticker.yaml) |  instruction for delivering [machineandme/ticker-backend-go](https://github.com/machineandme/ticker-backend-go)|
|[`./playbooks/machines/dvarghare.yaml`](https://github.com/machineandme/machineand.me/tree/master/playbooks/machines/dvarghare.yaml) |  instruction for delivering [machineandme/dvarghare-backend-go](https://github.com/machineandme/dvarghare-backend-go)


## Links to servers

| Project | Production | Test |
|-|-|-|
| Machine and me landing | [machineand.me](https://machineand.me) | [test.machineand.me](https://test.machineand.me) |
| Codetee | [codetee.machineand.me](https://codetee.machineand.me) | [testcodetee.machineand.me](https://testcodetee.machineand.me) |
| Ticker | [ticker.love](https://ticker.love) | [test.ticker.love](https://test.ticker.love) |
| Dvarghare landing | [dvärghare.com](https://dvärghare.com) | [test.dvärghare.com](https://test.dvärghare.com) |
| Dvarghare api | [api.dvärghare.com](https://api.dvärghare.com) | [testapi.dvärghare.com](https://testapi.dvärghare.com) |