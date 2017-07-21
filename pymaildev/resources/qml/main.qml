import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3
import QtQuick.Window 2.2

ApplicationWindow {
    //visible: true
    width: 1200
    height: 800
    title: qsTr("PyMailDev")

    menuBar: MenuBar {
        Menu {
            title: qsTr("&File")
            MenuItem {
                text: qsTr("Options")
                onTriggered: dialogAccount.open()
            }
            AccountParams { id: dialogAccount }
            MenuSeparator {}
            MenuItem {
                text: qsTr("Exit")
                onTriggered: Qt.quit()
            }
        }
    }

    toolBar: ToolBar {
        RowLayout {
            anchors.fill: parent
            ToolButton {
                text: qsTr("New mail")
            }
            ToolButton {
                text: qsTr("Delete")
                //iconSource: "img.ext"
            }
            ToolButton {
                text: qsTr("Reply")
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
}
