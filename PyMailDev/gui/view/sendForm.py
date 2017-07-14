import pyforms
import emails
from   pyforms          import BaseWidget
from   pyforms.Controls import ControlText
from   pyforms.Controls import ControlButton
from   pyforms.Controls import ControlTextArea
from   PyMailDev.gui.model.email import Email
from   PyMailDev.core.config.conf import Conf


class SendForm(BaseWidget):
    def __init__(self):
        super(SendForm, self).__init__('Send email')

        # Definition of the forms' fields
        self._fullName      = ControlText('Full Name', 'NOM PRENOM')
        self._ffrom         = ControlText('From', 'Adresse1@gmail.com')
        self._to            = ControlText('To', 'Adresse2@test.fr')
        self._cc            = ControlText('Cc')
        self._cci           = ControlText('Cci')
        self._subject       = ControlText('Subject')
        self._message       = ControlTextArea('Message', 'Mail envoyé depuis PyMailESGI')
        self._send          = ControlButton('Send')
        self._clear         = ControlButton('Clear Message')
        self._logs         = ControlTextArea('Logs')
        self._logs.readonly = True

        # Define the organization of the form
        self.formset = [('_fullName', '_ffrom', '_to'), '_cc', '_cci', '_subject',
                        '_message', ('_send', '_clear'), '_logs']

        # Define the button actions
        self._send.value = self.__sendAction
        self._clear.value = self.__clearAction

    def __sendAction(self):
        message = emails.html(html=self._message.value,
                              subject=self._subject.value,
                              mail_from=(self._fullName.value, self._ffrom.value))

        response = message.send(render={"project_name": "user/project1", "build_id": 121},
                                to=self._to.value,
                                smtp={"host": "smtp.gmail.com", "port": 465, "ssl": True,
                                      "user": "olvini33", "password": "Firegloww33"})

        assert response.status_code == 250
        self._logs.value += "Email sent to " + self._to.value + "\n"

    def __clearAction(self):
        self._message.value = ''

# Execute the application
if __name__ == "__main__":
    pyforms.start_app(SendForm, geometry=(810, 540, 800, 400))
