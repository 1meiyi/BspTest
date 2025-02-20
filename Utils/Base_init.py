import logging
import paramiko


class BspTest:
    ssh = None

    def __init__(self, host='192.168.117.87'):
        self.ssh = paramiko.SSHClient()
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.log = logging.getLogger(self.__class__.__name__)
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.ssh.connect(host, port=22, username='swqa', password='gfx123456')
            self.log.info('Connected to %s successfully.', host)
        except Exception as e:
            self.log.error('Failed to connect to %s: %s', host, e)
            raise

    def close(self):
        self.ssh.close()

    def send(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        stdout = stdout.read().decode()
        stderr = stderr.read().decode()
        if stdout:
            print(stdout)
            self.log.info('sucess ：\n%s', stdout.strip())
        else:
            self.log.warning('None output')
        if stderr:
            self.log.error('error：\n%s', stderr.strip())
        if stdin:
            self.log.info(f'exec cmd：%s', cmd)
        return stdin, stderr, stdout

# def login():
#     test = BspTest()
#     test.login('192.168.117.87')
#     test.send('ls -l')
#     test.close()
