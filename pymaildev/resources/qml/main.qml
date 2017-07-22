import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3
import QtQuick.Window 2.2

ApplicationWindow {
    id: root
    //visible: true
    width: 1200
    height: 800
    title: qsTr("PyMailDev")

    property variant winMail;

    menuBar: MenuBar {
        Menu {
            title: qsTr("&File")
            MenuItem {
                text: qsTr("Options")
                iconSource: "../icons/16x16/Application.png"
                onTriggered: dialogAccount.open()
                shortcut: StandardKey.Preferences
            }
            AccountParams { id: dialogAccount }
            MenuSeparator {}
            MenuItem {
                text: qsTr("Exit")
                iconSource: "../icons/16x16/Exit.png"
                onTriggered: Qt.quit()
                shortcut: StandardKey.Quit
            }
        }
        Menu {
            title: qsTr("&Edit")
            MenuItem {
                text: qsTr("Cut")
                shortcut: StandardKey.Cut
                //onTriggered:
                iconSource: "../icons/16x16/Cut.png"
                //iconName: "Cut"
                enabled: false
            }
            MenuItem {
                text: qsTr("Copy")
                shortcut: StandardKey.Copy
                //onTriggered:
                iconSource: "../icons/16x16/Copy.png"
                iconName: "Copy"
                enabled: false
            }
            MenuItem {
                text: qsTr("Paste")
                shortcut: StandardKey.Paste
                //onTriggered:
                iconSource: "../icons/16x16/Paste.png"
                iconName: "Paste"
                enabled: false
            }
        }
    }

    toolBar: ToolBar {
        RowLayout {
            anchors.fill: parent
            Layout.fillWidth: true
            ToolButton {
                action: newmailAction
                iconSource: "../icons/24x24/Create.png"
            }
            ToolButton {
                action: deletelAction
                iconSource: "../icons/24x24/Erase.png"
            }
            ToolBarSeparator {}
            ToolButton {
                action: replyAction
                //iconSource:
            }
            ToolButton {
                action: replyAllAction
                //iconSource:
            }
            ToolButton {
                action: transfertAction
                //iconSource:
            }
            Item { Layout.fillWidth: true }
        }
    }

    MainForm {
        anchors.fill: parent
        /*mouseArea.onClicked: {
            console.log(qsTr('Clicked on background. Text: "' + textEdit.text + '"'))
        }*/
    }

    statusBar: StatusBar {
        Label { text: qsTr("...") }
    }

    Action {
        id: newmailAction
        text: qsTr("New mail")
        shortcut: StandardKey.New
        onTriggered: {
            var component = Qt.createComponent("mail.qml");
            winMail = component.createObject(root);
            winMail.show();
        }
    }
    Action {
        id: deletelAction
        text: qsTr("Delete")
        shortcut: StandardKey.Delete
        enabled: false
    }
    Action {
        id: replyAction
        text: qsTr("Reply")
        enabled: false
    }
    Action {
        id: replyAllAction
        text: qsTr("Reply All")
        enabled: false
    }
    Action {
        id: transfertAction
        text: qsTr("Transfert")
        enabled: false
    }
}
