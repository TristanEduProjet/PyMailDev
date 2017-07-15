class Email(object):

    def __init__(self, fullName, ffrom, to, cc, cci, subject, message):
        self._fullName      = fullName
        self._ffrom         = ffrom
        self._to            = to
        self._cc            = cc
        self._cci           = cci
        self._subject       = subject
        self._message       = message

    @property
    def display(self):
        return "{0} {1} {2} {3} {4} {5} {6}"\
            .format(self._fullName, self._ffrom, self._to, self._cc,
                    self._cci, self._subject, self._message)
