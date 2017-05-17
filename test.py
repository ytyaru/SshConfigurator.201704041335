import os.path
import subprocess
import shlex
import paramiko
path_dir_ssh = os.path.join(os.path.expanduser('~'), '.ssh/')
path_file_config = os.path.join(path_dir_ssh, 'config')
config = paramiko.SSHConfig()
config.parse(open(path_file_config, 'r'))
for host in config.get_hostnames():
    print(host)
for host in config.get_hostnames():
    print(ssh_config.lookup(host))

