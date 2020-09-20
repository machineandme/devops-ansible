# Main deployment repository of machine and me

[![Deliver](https://github.com/machineandme/machineand.me/workflows/Deliver/badge.svg)](https://github.com/machineandme/machineand.me/actions)

Repository using ansible and github actions.

## Content

Any repository stored at [`./data/`](https://github.com/machineandme/machineand.me/tree/master/data):

+ Folder [`./data/server`](https://github.com/machineandme/machineand.me/tree/master/data/server) is static files, like HTML and CSS, for website [machineand.me](https://machineand.me)
+ Submodule `./data/shirts/` is link to [github.com/machineandme/shirts](https://github.com/machineandme/shirts)
+ Submodule `./data/ticker/` is link to [github.com/machineandme/ticker-backend](https://github.com/machineandme/ticker-backend)

## Ansible

### About ansible

+ Ansible configuration file [`./ansible.cfg`](https://github.com/machineandme/machineand.me/tree/master/ansible.cfg)  
    [Ansible config simple info](https://docs.ansible.com/ansible/2.9/installation_guide/intro_configuration.html#configuration-file)
+ Ansible inventory is list of server used for deploy [`./inventory.cfg`](https://github.com/machineandme/machineand.me/tree/master/inventory.cfg)  
    [Ansible inventory simple info](https://docs.ansible.com/ansible/2.9/network/getting_started/first_inventory.html)

### About playbooks
+ Playbooks is deploy steps [`./playbooks/`](https://github.com/machineandme/machineand.me/tree/master/playbooks)  
    [Ansible playbook simple info](https://docs.ansible.com/ansible/2.9/user_guide/playbooks.html)
+ Datadog playbook installs and setup datadog on server [`./playbooks/datadog.yaml`](https://github.com/machineandme/machineand.me/tree/master/playbooks/datadog.yaml)
+ Deploy playbook used for deploy our apps [`./playbooks/deploy.yaml`](https://github.com/machineandme/machineand.me/tree/master/playbooks/deploy.yaml)
+ Tasks is reusable steps of build, deploy or any [`./playbooks/tasks/`](https://github.com/machineandme/machineand.me/tree/master/playbooks/tasks)

### About playbook tasks

+ [`./playbooks/tasks/upload.yaml`](https://github.com/machineandme/machineand.me/tree/master/playbooks/tasks/upload.yaml) is used for upload static, configs and app data to target server.
+ [Caddy](http://caddyserver.com) is simplest _Auto-HTTPS_ server. [`./playbooks/tasks/caddy.yaml`](https://github.com/machineandme/machineand.me/tree/master/playbooks/tasks/caddy.yaml) is instruction to copy [`Caddyfile`](https://github.com/machineandme/machineand.me/blob/master/data/server/Caddyfile) and setup Caddy as server.
+ [`./playbooks/tasks/shirts.yaml`](https://github.com/machineandme/machineand.me/tree/master/playbooks/tasks/shirts.yaml) used to deliver [machineandme/shirts](https://github.com/machineandme/shirts)
+ [`./playbooks/tasks/ticker.yaml`](https://github.com/machineandme/machineand.me/tree/master/playbooks/tasks/ticker.yaml)  used to deliver [machineandme/ticker-backend](https://github.com/machineandme/ticker-backend)