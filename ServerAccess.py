'''
ServerAccess is a library for accessing & manipulating a Linux box.

@author: Scott McCammon
'''

import paramiko
from ServerInfo import ServerInfo

class ServerAccess(ServerInfo):
    """
    Paramiko wrapper to create an SSH connection & run commands on a Linux box.

    Typical usage:
        server_access = ServerAccess('host', 'user', 'password')
        server_access.run("git --version")
        server_access.run_sudo("dmesg")
    """
    def __init__(self, host, user_name, password):
        ServerInfo.__init__(self, host, user_name, password)
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def run(self, cmd):
        """
        Interactive shell
        :param cmd: Command to execute (string)
        :return : Tuple of output (List of Strings) & error (List of Strings)
        """
        if cmd:
            print cmd
            try:
                self._ssh_connect()
                stdin, stdout, stderr = self.ssh.exec_command(cmd)
                response = stdout.read().splitlines()
                error = stderr.read().splitlines()
                self._ssh_disconnect()
                return response, error
            except Exception as e:
                print e
                return None

    def run_sudo(self, cmd):
        """
        Interactive shell with sudo rights

        :param cmd: Command to execute as sudo (String)
        :return : Tuple of output (List of Strings) & error (List of Strings)
        """
        if cmd:
            cmd = "sudo -k " + cmd  # -k forces password
            print cmd
            try:
                self._ssh_connect()
                transport = self.ssh.get_transport()
                session = transport.open_session()
                session.set_combine_stderr(True)
                session.get_pty()
                session.exec_command(cmd)
                stdin = session.makefile('wb', -1)
                stdout = session.makefile('rb', -1)

                # Type password for sudo access
                stdin.write(self.password + '\n')
                stdin.flush()
                response = stdout.read().splitlines()
                self._ssh_disconnect()
                return response
            except Exception as e:
                print e
                return None

    def _ssh_connect(self):
        """
        Paramiko wrapper around connect method
        """
        self.ssh.connect(self.host, username=self.user_name, password=self.password)

    def _ssh_disconnect(self):
        """
        Paramiko wrapper around close method
        """
        self.ssh.close()



#if __name__ == '__main__':
    #server_access = ServerAccess('host', 'username', 'pw')
    #print server_access.run("uname -s")
    #print server_access.run("uptime")
    #print server_access.run("ls")
    #print server_access.run("git --version")
    #print server_access.run_sudo("dmesg")
    #print server_access.run('')
    #print server_access.run('ll')

    #print 'Complete'