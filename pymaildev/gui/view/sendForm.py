import emails
import pyforms
from   pyforms import BaseWidget
from   pyforms.Controls import ControlButton
from   pyforms.Controls import ControlText
from   pyforms.Controls import ControlTextArea
from   pymaildev.gui.model.email import Email


class SendForm(Email, BaseWidget):
    """
    Email reply window
    """
    def __init__(self):
        Email.__init__(self, '', '', '', '', '', '', '')
        BaseWidget.__init__(self, 'Send Email')

        BaseWidget.set_margin(self, 10)

        # Definition of the forms' fields
        self._fullname      = ControlText('Full Name', 'Lefebvre Olivier')
        self._from          = ControlText('From', 'olvini33@gmail.com')
        self._to            = ControlText('To', 'olivier.lefebvre@akeonet.com')
        self._cc            = ControlText('Cc')
        self._cci           = ControlText('Cci')
        self._subject       = ControlText('Subject')
        self._message       = ControlTextArea('Message', 'Mail envoyé depuis PyMailESGI')
        self._send          = ControlButton('Send')
        self._clear         = ControlButton('Clear Message')
        self._logs          = ControlTextArea('Logs')
        self._logs.readonly = True

        # Define the organization of the form
        self.formset = [('_fullname', '_from', '_to'), '_cc', '_cci', '_subject',
                        '_message', ('_send', '_clear'), '_logs']

        # Define the button actions
        self._send.value = self.__sendAction
        self._clear.value = self.__clearAction

    def __sendAction(self):
        """
        Send button event
        :return:
        """
        # Retrieve the form' ControlText values to compose the Email to send
        try:
            message = emails.html(html=self._message.value, subject=self._subject.value,
                                  mail_from=(self._fullname.value, self._from.value))
        except Exception:
            self._logs.value += "Error: Incorrect entered values.\n"
            raise

        # Send the message with the parameters formerly defined
        try:
            response = message.send(to=self._to.value,
                                    smtp={"host": "smtp.gmail.com", "port": 465, "ssl": True,
                                          "user": "A CHANGER", "password": "A CHANGER"})
        except Exception:
            self._logs.value += "Error: Incorrect SMTP configuration.\n"
            raise

        # Assert the email has been correctly sent and received by the recipient
        assert response.status_code == 250

        if response.status_code == 250:
            self._logs.value += "Email sent to " + self._to.value + ".\n"
            # TODO: Stocker l'email envoyé dans une autre liste graphique ?

    def __clearAction(self):
        """
        Clear button event. Reset the textarea '_message' value.
        :return:
        """
        self._message.value = ''
