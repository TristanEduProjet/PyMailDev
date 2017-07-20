import QtQuick 2.4
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3
import QtQuick.Controls.Styles.Desktop 1.0

Item {
    width: 800
    height: 600
    property alias columnLayout: columnLayout

    ColumnLayout {
        id: columnLayout
        spacing: 5
        anchors.fill: parent

        RowLayout {
            width: 100
            height: 100
            Layout.fillWidth: true

            Text {
                text: qsTr("From :")
                transformOrigin: Item.Left
                verticalAlignment: Text.AlignVCenter
                textFormat: Text.PlainText
                font.pixelSize: 12
            }

            TextField {
                id: textFrom
                text: qsTr("Text Field")
                transformOrigin: Item.Right
                Layout.fillWidth: true
            }
        }

        RowLayout {
            width: 100
            height: 100
            Text {
                text: qsTr("To :")
                textFormat: Text.PlainText
                font.pixelSize: 12
                verticalAlignment: Text.AlignVCenter
                transformOrigin: Item.Left
            }

            TextField {
                id: textTo
                text: qsTr("Text Field")
                transformOrigin: Item.Right
                Layout.fillWidth: true
            }
            Layout.fillWidth: true
        }

        RowLayout {
            width: 100
            height: 100
            Text {
                text: qsTr("Cc :")
                textFormat: Text.PlainText
                font.pixelSize: 12
                verticalAlignment: Text.AlignVCenter
                transformOrigin: Item.Left
            }

            TextField {
                id: textCc
                text: qsTr("Text Field")
                transformOrigin: Item.Right
                Layout.fillWidth: true
            }
            Layout.fillWidth: true
        }

        RowLayout {
            width: 100
            height: 100
            Text {
                text: qsTr("Cci :")
                textFormat: Text.PlainText
                font.pixelSize: 12
                verticalAlignment: Text.AlignVCenter
                transformOrigin: Item.Left
            }

            TextField {
                id: textCci
                text: qsTr("Text Field")
                transformOrigin: Item.Right
                Layout.fillWidth: true
            }
            Layout.fillWidth: true
        }

        RowLayout {
            width: 100
            height: 100
            Text {
                text: qsTr("Subject :")
                textFormat: Text.PlainText
                font.pixelSize: 12
                verticalAlignment: Text.AlignVCenter
                transformOrigin: Item.Left
            }

            TextField {
                id: textSubject
                text: qsTr("Text Field")
                transformOrigin: Item.Right
                Layout.fillWidth: true
            }
            Layout.fillWidth: true
        }

        ColumnLayout {
            width: 100
            height: 100
            Layout.fillWidth: true

            TextArea {
                id: msgArea
                text: qsTr("Text Area")
                Layout.fillHeight: true
                Layout.fillWidth: true
            }
        }

        RowLayout {
            width: 100
            height: 100
            Layout.fillWidth: true

            Button {
                id: btnSend
                text: qsTr("Send")
                Layout.fillWidth: true
            }

            Button {
                id: btnClear
                text: qsTr("Clear message")
                Layout.fillWidth: true
            }
        }

        ColumnLayout {
            width: 100
            Layout.fillWidth: true

            TextArea {
                id: logArea
                text: qsTr("Log Area")
                enabled: false
                Layout.fillHeight: true
                Layout.fillWidth: true
            }
        }
    }
}
