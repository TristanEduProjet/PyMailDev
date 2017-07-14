import pickle


class Emails(object):

    def __init__(self):
        self._emails = []

    def addEmail(self, person):
        self._emails.append(person)

    def removeEmail(self, index):
        return self._emails.pop(index)

    def save(self, filename):
        output = open(filename, 'wb')
        pickle.dump(self._emails, output)

    def load(self, filename):
        pkl_file = open(filename, 'rb')
        self._emails = pickle.load(pkl_file)
