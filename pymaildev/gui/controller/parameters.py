import pickle


class Parameters:
    """
    Parameters controller
    !!! INCOMPLET ET OBSOLETE !!!
    """
    def __init__(self):
        self._params = {}

    def save_parameters(self, host, port, ssl, user, password):
        # Create the file or append at the end-of-file
        self._params = {"host": host,
                        "port": port,
                        "ssl": ssl,
                        "user": user,
                        "password": password}
        pickle.dump(self._params, open("PyMailDev/resources/parameters.ini", "wb"))

    def load_parameters(self):
        # Get parameters from parameters.ini
        self._params = pickle.load(open("PyMailDev/resources/parameters.ini", "rb"))
