import logging
import paramiko
import re
from Utils.OperationData import OperationData
from collections import ChainMap
from time import sleep


class BspTest:
    ssh = None

    def __init__(self):
        logging.basicConfig(level=logging.INFO, format='\n%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.ssh = paramiko.SSHClient()
        self.log = logging.getLogger(__name__)
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def login(self, host):
        try:
            self.ssh.connect(host, port=22, username='swqa', password='gfx123456')
            self.log.info('Connected to %s successfully.', host)
        except Exception as e:
            self.log.error('Failed to connect to %s: %s', host, e)
            raise

    def send(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        stdout = stdout.read().decode()
        return stdout
    def close(self):
        self.ssh.close()
