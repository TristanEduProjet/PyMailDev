import pickle


class Emails(object):
    """
    Emails controller
    !!! INCOMPLET ET OBSOLETE !!!
    """
    def __init__(self):
        self._emails = []

    def addEmail(self, person):
        self._emails.append(person)

    def removeEmail(self, index):
        return self._emails.pop(index)

    def save(self, filename):
        output = open(filename, 'w')
        pickle.dump(self._emails, output)

    def load(self, filename):
        pkl_file = open(filename, 'r')
        self._emails = pickle.load(pkl_file)
