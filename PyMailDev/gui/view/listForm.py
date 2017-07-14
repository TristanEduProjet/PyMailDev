import pyforms
from   pyforms          import BaseWidget
from   pyforms.Controls import ControlText
from   pyforms.Controls import ControlButton
from   PyMailESGI.model.email import Email


class ListForm(Email, BaseWidget):
    def __init__(self):
        Email.__init__(self, '', '', '')
        BaseWidget.__init__(self, 'Emails')

        # Definition of the forms fields
        self._fullName      = ControlText('Full Name')
        self._from          = ControlText('From')
        self._subject        = ControlText('Subject')
        self._message       = ControlText('Message')
        self._reply         = ControlButton('Reply')

        # Define the button action
        self._reply.value = self.__replyAction

    def __replyAction(self):
        self._firstName             = self._firstnameField.value
        self._middleName            = self._middlenameField.value
        self._lastName              = self._lastnameField.value
        self._fullnameField.value   = self.fullName

        # In case the window has a parent
        if self.parent is not None:
            self.parent.addEmail(self)

# Execute the application
if __name__ == "__main__":
    pyforms.start_app(ListForm)
