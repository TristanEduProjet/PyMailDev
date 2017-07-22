import QtQuick 2.4
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles.Desktop 1.0
import QtQuick.Layouts 1.3
import QtQuick.Dialogs 1.2

Dialog {
    width: 420
    height: 300
    title: qsTr("Account parameter")
    modality: Qt.WindowModal

    signal onCancel()
    signal onValidate()

    onRejected: console.log("dialog account : Rejected")
    onAccepted: console.log("dialog account : Accepted")
    onButtonClicked: console.log("dialog account : clicked button " + clickedButton)
    //onHelp:
    onApply: console.log("dialog account : Apply")
    //onReset:
    onDiscard: console.log("dialog account : Discard")

    contentItem: AccountParamsForm {
        anchors.fill: parent
        anchors.margins: 4
        Layout.fillHeight: true
        Layout.fillWidth: true

        btnCancel.onClicked: onCancel()
        btnSave.onClicked: onValidate()

        receiveType.model: listReceive
        receiveType.onCurrentIndexChanged: console.log(listReceive.get(receiveType.currentIndex).text)
        receiveSSL.model: listSSL
        receiveSSL.onCurrentIndexChanged: console.log(listSSL.get(receiveSSL.currentIndex).text)

        sendType.model: listSend
        sendType.onCurrentIndexChanged: console.log(listSend.get(sendType.currentIndex).text)
        sendSSL.model: listSSL
        sendSSL.onCurrentIndexChanged: console.log(listSSL.get(sendSSL.currentIndex).text)
    }

    ListModel {
        id: listSend
        ListElement {
            text: "SMTP"
        }
    }

    ListModel {
        id: listReceive
        ListElement {
            text: "POP3"
        }
        ListElement {
            text: "IMAP"
        }
    }

    ListModel {
        id: listSSL
        ListElement {
            text: "En clair"
        }
        ListElement {
            text: "StatTLS"
        }
        ListElement {
            text: "SSL/TLS"
        }
    }
}

/*
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
*/
