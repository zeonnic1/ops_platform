from paramiko.client import SSHClient, AutoAddPolicy
from paramiko.rsakey import RSAKey
from paramiko.ssh_exception import SSHException, AuthenticationException, NoValidConnectionsError
from io import StringIO


class SSH(object):

    def __init__(self, hostname, port=22, username="root", password=None, pkey=None, connect_timeout=10):
        self.params = {
            "hostname": hostname,
            "port": port,
            "username": username,
            "password": password,
            "pkey": RSAKey.from_private_key(StringIO(pkey)) if isinstance(pkey, str) and len(pkey) != 0 else pkey,
            "timeout": connect_timeout
        }

        if not pkey:
            del self.params["pkey"]
        if not password:
            del self.params["password"]
        if not pkey and not password:
            raise SSHException("密码和密钥必须选择输入一个")
        self.client = None

    def connect(self):
        self.client = SSHClient()
        self.client.set_missing_host_key_policy(AutoAddPolicy)
        self.client.connect(**self.params)
        print("成功连接")

    def ping(self):
        if self.client:
            raise RuntimeError("已建立连接")
        else:
            try:
                self.connect()
            except(TimeoutError, AuthenticationException, NoValidConnectionsError, Exception):
                return None
        return True


# if __name__ == '__main__':
#     client = SSH('127.0.0.1', 9922, "root", "123")
#     client.connect()
