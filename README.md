# Ansible Role: EPEL Repository

[![CI](https://github.com/geerlingguy/ansible-role-repo-epel/actions/workflows/ci.yml/badge.svg)](https://github.com/geerlingguy/ansible-role-repo-epel/actions/workflows/ci.yml)

Installs the [EPEL repository](https://fedoraproject.org/wiki/EPEL) (Extra Packages for Enterprise Linux) for RHEL/CentOS.

## Requirements

This role only is needed/runs on RHEL and its derivatives.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    epel_repo_url: "http://download.fedoraproject.org/pub/epel/{{ ansible_distribution_major_version }}/{{ ansible_userspace_architecture }}{{ '/' if ansible_distribution_major_version < '7' else '/e/' }}epel-release-{{ ansible_distribution_major_version }}-{{ epel_release[ansible_distribution_major_version] }}.noarch.rpm"
    epel_repo_gpg_key_url: "/etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-{{ ansible_distribution_major_version }}"

The EPEL repo URL and GPG key URL. Generally, these should not be changed, but if this role is out of date, or if you need a very specific version, these can both be overridden.

    epel_repo_disable: false

Set to `true` to disable the EPEL repo (even if already installed).

## Dependencies

None.

## Example Playbook

    - hosts: servers
      roles:
        - geerlingguy.repo-epel

## License

MIT / BSD

## Author Information

This role was created in 2014 by [Jeff Geerling](https://www.jeffgeerling.com/), author of [Ansible for DevOps](https://www.ansiblefordevops.com/).
