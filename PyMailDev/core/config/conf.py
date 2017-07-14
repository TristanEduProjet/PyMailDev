class Conf:
    host = None
    port = None
    ssl = None
    user = None
    password = None

    def __init__(self):
        self._host = Conf.host
        self._port = Conf.port
        self._ssl = Conf.ssl
        self._user = Conf.user
        self._password = Conf.password

    def _get_host(self):
        return self._host

    def _get_port(self):
        return self._port

    def _get_ssl(self):
        return self._ssl

    def _get_user(self):
        return self._user

    def _get_password(self):
        return self._password

    def _set_host(self, host):
        self._host = host

    def _set_port(self, port):
        self._port = port

    def _set_ssl(self, ssl):
        self._ssl = ssl

    def _set_user(self, user):
        self._user = user

    def _set_password(self, password):
        self._password = password

    host = property(_get_host, _set_host)
    port = property(_get_port, _set_port)
    ssl = property(_get_ssl, _set_ssl)
    user = property(_get_user, _set_user)
    password = property(_get_password, _set_password)

    def _get_infos(self):
        """Parcourir un fichier où seront stockées les informations de cette classe"""
