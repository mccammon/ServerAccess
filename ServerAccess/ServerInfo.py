'''
ServerInfo is an object to keep track of server information.

@author: Scott McCammon
'''

class ServerInfo(object):
    """
    Server information object

    """

    def __init__(self, host, user_name, password):
        """
        Create a new ServerInfo
        """
        self.host = host
        self.user_name = user_name
        self.password = password
