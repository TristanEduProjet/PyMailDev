import pyforms
from   pyforms import BaseWidget
from   pyforms.Controls import ControlButton
from   pyforms.Controls import ControlList
from   pyforms.Controls import ControlEmptyWidget
from   pymaildev.gui.model.email import Email
from   pymaildev.gui.controller.emails import Emails
from   pymaildev.gui.view.parametersForm import ParametersForm
from   pymaildev.gui.view.sendForm import SendForm


class ListForm(BaseWidget):
    """
    Listed emails' window
    """
    emails = []

    def __init__(self):
        BaseWidget.__init__(self, 'Emails')

        BaseWidget.set_margin(self, 10)

        # Definition of the forms fields
        self._param_panel               = ControlEmptyWidget("Email configuration")
        self._reply_panel               = ControlEmptyWidget("Send Email")
        self._reply                     = ControlButton('Reply')
        self._delete                    = ControlButton('Delete')
        self._options                   = ControlButton('Options')
        self._emails                    = ControlList("Emails")

        self._emails.readonly           = True
        self._emails.select_entire_row  = True
        self.__load_emails()  # TODO: Charger tous les Email dans la ControlList au démarrage
        self._param_panel.hide()
        self._reply_panel.hide()

        # Define the organization of the form
        self.formset = ['_emails', ('_delete', '_options', '_reply')]

        # Define the button action
        self._reply.value = self.__replyAction
        self._options.value = self.__optionsAction
        self._delete.value = self.__deleteAction

    def __replyAction(self):
        """
        Reply button event
        :return:
        """
        # TODO: Récupérer données de la ligne de l'email et les insérer dans un objet Email

        # Load SendForm
        reply_form = SendForm()
        reply_form.parent = self
        self._reply_panel.value = reply_form
        self._reply_panel.show()

    def __deleteAction(self):
        """
        Delete button event
        :return:
        """
        """ TODO: Supprimer email.s coché.s """
        # self._emails.__sub__(0)

    def __optionsAction(self):
        """
        Options button event
        :return:
        """
        # Load ParametersForm
        param_form = ParametersForm()
        param_form.parent = self
        self._param_panel.value = param_form
        self._param_panel.show()

    def __load_emails(self):
        """
        Load all Email objects et insert them into the ControlList
        :return:
        """
        """Charger tous les objets Email, et les insérer dans la ControlList"""
        # Note : Peut-être utiliser la fonction 'set_value(column, row, value)' pour chaque Email sur lesquels on boucle


# Execute the application
if __name__ == "__main__":
    pyforms.start_app(ListForm, geometry=(810, 540, 800, 400))
