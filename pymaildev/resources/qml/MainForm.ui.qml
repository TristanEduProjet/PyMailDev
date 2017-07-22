import QtQuick 2.6
import QtQuick.Templates 2.2
import QtQuick.Controls 1.4
import QtQuick.Dialogs.qml 1.0
import QtQuick.Controls.Styles.Desktop 1.0
import QtQuick.Controls.Universal 2.0
import QtQuick.Layouts 1.3
import QtQuick.LocalStorage 2.0
import QtQuick.Extras 1.4

Rectangle {
    width: 660
    height: 460

    property variant tree: treeView
    property variant table: tableView
    property variant text: textArea

    SplitView {
        anchors.fill: parent

        TreeView {
            id: treeView
            width: 260
            anchors.right: splitView.left
            anchors.rightMargin: 0
            anchors.left: parent.left
            anchors.leftMargin: 0
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 0
            anchors.top: parent.top
            anchors.topMargin: 0
            Layout.fillWidth: true
            horizontalScrollBarPolicy: Qt.ScrollBarAlwaysOn
            verticalScrollBarPolicy: Qt.ScrollBarAlwaysOn
        }

        SplitView {
            id: splitView
            width: 500
            anchors.left: treeView.right
            anchors.leftMargin: 0
            anchors.right: parent.right
            anchors.rightMargin: 0
            anchors.top: parent.top
            anchors.topMargin: 0
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 0
            orientation: Qt.Vertical
            Layout.fillWidth: true

            TableView {
                id: tableView
                anchors.bottom: textArea.top
                anchors.bottomMargin: 0
                anchors.right: parent.right
                anchors.rightMargin: 0
                anchors.left: parent.left
                anchors.leftMargin: 0
                anchors.top: parent.top
                anchors.topMargin: 0
                Layout.fillWidth: true
                verticalScrollBarPolicy: Qt.ScrollBarAlwaysOn
                TableViewColumn {
                    title: qsTr("From")
                    role: "from"
                }
                TableViewColumn {
                    title: qsTr("Object")
                    role: "object"
                }
                TableViewColumn {
                    title: qsTr("Date")
                    role: "sendOn"
                }
                model: tableModel
            }

            TextArea {
                id: textArea
                readOnly: true
                anchors.top: tableView.bottom
                anchors.topMargin: 0
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 0
                anchors.right: parent.right
                anchors.rightMargin: 0
                anchors.left: parent.left
                anchors.leftMargin: 0
                Layout.fillWidth: true
                horizontalScrollBarPolicy: Qt.ScrollBarAlwaysOn
                verticalScrollBarPolicy: Qt.ScrollBarAlwaysOn
            }
        }
    }
}
