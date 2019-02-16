import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_epel_repo_file_should_exist(host):
    epel_repo_file = host.file('/etc/yum.repos.d/epel.repo')

    assert epel_repo_file.exists


def test_yum_should_install_packages_in_epel_repo(host):
    yum_install_return_code = host.run('yum install -y htop').rc

    assert yum_install_return_code == 0


def test_installed_package_should_run(host):
    htop_return_code = host.run('htop --version').rc

    assert htop_return_code == 0
