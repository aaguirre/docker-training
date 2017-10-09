# Lab 07: Automate!

## Ansible:

Ansible is the simplest way to automate apps and IT infrastructure. Application Deployment + Configuration Management + Continuous Delivery

https://www.ansible.com


Ansible Project

```vim
.
├── envs
│   └── development
│       ├── group_vars
│       │   └── all.yml
│       └── hosts
├── play.yml
└── roles
    ├── build
    │   └── tasks
    │       └── main.yml
    └── deploy
        └── tasks
            └── main.yml
```


Install Ansible
```bash
pip install ansible
```

Execute Ansible Playbook

```bash
ansible-playbook -i envs/development/hosts play.yml --tags="build,deploy"  -vvv
```

Go to url:

http://machine-ip:80
