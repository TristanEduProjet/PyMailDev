import QtQuick 2.4
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles.Desktop 1.0
import QtQuick.Layouts 1.3
import QtPositioning 5.9

ColumnLayout {
    spacing: 5

    RowLayout {
        Layout.fillWidth: true
        Text {
            text: qsTr("Nom du compte :")
            font.pixelSize: 12
        }
        TextField {
            id: textName
            placeholderText: qsTr("Perso")
            Layout.fillWidth: true
        }
    }

    RowLayout {
        Layout.fillWidth: true
        Text {
            text: qsTr("Adresse :")
            font.pixelSize: 12
        }
        TextField {
            id: textMail
            placeholderText: qsTr("adr@domain.com")
            Layout.fillWidth: true
        }
    }

    RowLayout {
        spacing: 10
        Layout.fillWidth: true
        RowLayout {
            spacing: 5
            Layout.fillWidth: true
            Text {
                text: qsTr("Nom d'utilisateur :")
                font.pixelSize: 12
            }
            TextField {
                id: textUser
                Layout.fillWidth: true
                placeholderText: qsTr("user")
            }
        }
        RowLayout {
            spacing: 5
            Layout.fillWidth: true
            Text {
                text: qsTr("Mot de passe :")
                font.pixelSize: 12
            }
            TextField {
                id: textPwd
                Layout.fillWidth: true
                placeholderText: qsTr("pwd")
                echoMode: TextInput.Password
            }
        }
    }

    GroupBox {
        title: qsTr("Serveur")
        Layout.fillWidth: true

        ColumnLayout {
            anchors.fill: parent
            Layout.fillWidth: true

            GroupBox {
                title: qsTr("Réception")
                Layout.fillWidth: true
                RowLayout {
                    spacing: 6
                    Layout.fillWidth: true

                    ComboBox {
                        id: comboxReceiveType
                        width: 50
                    }
                    ComboBox {
                        id: comboxReceiveSSL
                        width: 80
                    }

                    Text {
                        text: qsTr("Host :")
                    }
                    TextField {
                        id: textReceiveHost
                        placeholderText: qsTr("recv.server.com")
                        Layout.fillWidth: true
                    }

                    Text {
                        text: qsTr("Port :")
                    }
                    TextField {
                        id: textReceivePort
                        width: 50
                        placeholderText: qsTr("123")
                    }
                }
            }

            GroupBox {
                title: qsTr("Envoi")
                Layout.fillWidth: true
                ColumnLayout {
                    Layout.fillWidth: true

                    RowLayout {
                        spacing: 6
                        Layout.fillWidth: true

                        ComboBox {
                            id: comboxSendType
                            width: 50
                        }
                        ComboBox {
                            id: comboxSendSSL
                            width: 80
                        }

                        Text {
                            text: qsTr("Host :")
                        }
                        TextField {
                            id: textSendHost
                            placeholderText: qsTr("smpt.domain.com")
                            Layout.fillWidth: true
                        }

                        Text {
                            text: qsTr("Port :")
                        }
                        TextField {
                            id: textSendPort
                            width: 50
                            placeholderText: qsTr("123")
                        }
                    }

                    GroupBox {
                        id: grpSendAuth
                        title: "Authentification différente"
                        checked: false
                        checkable: true
                        Layout.fillWidth: true
                        RowLayout {
                            Layout.fillWidth: true

                            RowLayout {
                                Layout.fillWidth: true
                                Text {
                                    text: qsTr("Nom d'utilisateur :")
                                    font.pixelSize: 12
                                }
                                TextField {
                                    id: textSendUser
                                    Layout.fillWidth: true
                                    placeholderText: qsTr("user")
                                }
                            }

                            RowLayout {
                                Layout.fillWidth: true
                                Text {
                                    text: qsTr("Mot de passe :")
                                    font.pixelSize: 12
                                }
                                TextField {
                                    id: textSendPsw
                                    Layout.fillWidth: true
                                    placeholderText: qsTr("psw")
                                    echoMode: TextInput.Password
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    RowLayout {
        Layout.fillWidth: true
        Button {
            id: btnCancel
            text: qsTr("Annuler")
            Layout.fillWidth: true
        }
        Button {
            id: btnSave
            text: qsTr("Valider")
            Layout.fillWidth: true
        }
    }
}
