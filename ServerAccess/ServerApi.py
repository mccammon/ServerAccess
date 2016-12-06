'''
ServerApi is the external facing methods for terminal commands.

@author: Scott McCammon
'''

from ServerAccess import ServerAccess
import time

class ServerApi(ServerAccess):
    def __init__(self, host, user_name, password):
        ServerAccess.__init__(self, host, user_name, password)

    def is_git_installed(self):
        output, error = self.run('git --version')
        if error:
            return False
        return True

    def install_git(self):
        if not self.is_git_installed():
            print self._apt_get('apt-get install git')

    def remove_git(self):
        if self.is_git_installed():
            print self._apt_get('apt-get remove git')

    def _apt_get(self, cmd):
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
                stdin.write(self.password + '\n')
                stdin.flush()
                #self.wait_for('Do you want to continue?', stdout)
                #line = 'Do you want to continue?'
                #match = False
                #while not match:
                #    response = stdout.read().splitlines()
                #    print response
                #    match = [s for s in response if line in s]
                #    print match
                time.sleep(10)
                stdin.write('Y\n')
                stdin.flush()
                response = stdout.read().splitlines()
                self._ssh_disconnect()
                return response
            except Exception as e:
                print e
                return None

#if __name__ == '__main__':
    #server = ServerApi('host', 'username', 'pw')
    #print server.is_git_installed()
    #server.install_git()
    #print server.is_git_installed()
    #server.remove_git()
    #print server.is_git_installed()
    #print 'Complete'