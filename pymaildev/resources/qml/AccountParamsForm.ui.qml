import QtQuick 2.4
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles.Desktop 1.0
import QtQuick.Layouts 1.3

ColumnLayout {
    spacing: 5

    property alias btnSave: btnSave
    property alias btnCancel: btnCancel
    property alias btnAutoDetect: autoDetect
    property bool newAccount: true

    property alias name: textName
    property alias mail: textMail
    property alias user: textUser
    property alias pwd: textPwd

    property alias receiveType: comboxReceiveType
    property alias receiveSSL: comboxReceiveSSL
    property alias receiveHost: textReceiveHost
    property alias receivePort: spinReceivePort

    property alias sendType: comboxSendType
    property alias sendSSL: comboxSendSSL
    property alias sendHost: textSendHost
    property alias sendPort: spinSendPort
    property alias sendAuth: grpSendAuth
    property alias sendUser: textSendUser
    property alias sendPsw: textSendPsw

    RowLayout {
        Layout.fillWidth: true
        Label {
            text: qsTr("Nom du compte :")
            verticalAlignment: Text.AlignVCenter
        }
        TextField {
            id: textName
            placeholderText: qsTr("Perso")
            Layout.fillWidth: true
        }
    }

    RowLayout {
        Layout.fillWidth: true
        Label {
            text: qsTr("Adresse :")
            verticalAlignment: Text.AlignVCenter
        }
        MailField {
            id: textMail
            Layout.fillWidth: true
        }

        Button {
            id: autoDetect
            text: qsTr("Auto-detect config.")
            transformOrigin: Item.Right
        }
    }

    RowLayout {
        spacing: 10
        Layout.fillWidth: true
        RowLayout {
            spacing: 5
            Layout.fillWidth: true
            Label {
                text: qsTr("Nom d'utilisateur :")
                verticalAlignment: Text.AlignVCenter
            }
            TextField {
                id: textUser
                Layout.fillWidth: true
                placeholderText: qsTr("user")
                inputMethodHints: Qt.ImhNoAutoUppercase
            }
        }
        RowLayout {
            spacing: 5
            Layout.fillWidth: true
            Label {
                text: qsTr("Mot de passe :")
                verticalAlignment: Text.AlignVCenter
            }
            PasswordField {
                id: textPwd
                Layout.fillWidth: true
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
                        width: 40
                    }
                    ComboBox {
                        id: comboxReceiveSSL
                        width: 40
                    }

                    Label {
                        text: qsTr("Host :")
                    }
                    TextField {
                        id: textReceiveHost
                        placeholderText: qsTr("recv.server.com")
                        Layout.fillWidth: true
                        inputMethodHints: Qt.ImhNoAutoUppercase
                    }

                    Label {
                        text: qsTr("Port :")
                    }
                    SpinBox {
                        id: spinReceivePort
                        stepSize: 1
                        maximumValue: 65535
                        minimumValue: 1
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
                            width: 40
                        }
                        ComboBox {
                            id: comboxSendSSL
                            width: 40
                        }

                        Label {
                            text: qsTr("Host :")
                        }
                        TextField {
                            id: textSendHost
                            placeholderText: qsTr("smpt.domain.com")
                            Layout.fillWidth: true
                            inputMethodHints: Qt.ImhNoAutoUppercase
                        }

                        Label {
                            text: qsTr("Port :")
                        }
                        SpinBox {
                            id: spinSendPort
                            stepSize: 1
                            maximumValue: 65535
                            minimumValue: 1
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
                                Label {
                                    text: qsTr("Nom d'utilisateur :")
                                    verticalAlignment: Text.AlignVCenter
                                }
                                TextField {
                                    id: textSendUser
                                    Layout.fillWidth: true
                                    placeholderText: qsTr("user")
                                    inputMethodHints: Qt.ImhNoAutoUppercase
                                }
                            }

                            RowLayout {
                                Layout.fillWidth: true
                                Label {
                                    text: qsTr("Mot de passe :")
                                    verticalAlignment: Text.AlignVCenter
                                }
                                PasswordField {
                                    id: textSendPsw
                                    Layout.fillWidth: true
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
