#!/usr/bin/env bash

# ssh config with private key
eval `ssh-agent`
ssh-add ~/.ssh/id_rsa

# remote deployment
. venv/bin/activate
ansible-playbook -i hosts playbook.yml --ask-become-pass
