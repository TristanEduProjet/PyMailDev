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
            Layout.fillWidth: true
            Text {
                text: qsTr("From:")
                transformOrigin: Item.Left
                verticalAlignment: Text.AlignVCenter
                textFormat: Text.PlainText
                font.pixelSize: 12
            }
            TextField {
                id: textFrom
                text: qsTr("From...")
                transformOrigin: Item.Right
                Layout.fillWidth: true
                enabled: false
            }
        }

        RowLayout {
            Layout.fillWidth: true
            Text {
                text: qsTr("To:")
                textFormat: Text.PlainText
                font.pixelSize: 12
                verticalAlignment: Text.AlignVCenter
                transformOrigin: Item.Left
            }
            TextField {
                id: textTo
                text: qsTr("To...")
                transformOrigin: Item.Right
                Layout.fillWidth: true
            }
        }

        RowLayout {
            Layout.fillWidth: true
            Text {
                text: qsTr("Cc:")
                textFormat: Text.PlainText
                font.pixelSize: 12
                verticalAlignment: Text.AlignVCenter
                transformOrigin: Item.Left
            }
            TextField {
                id: textCc
                text: qsTr("Cc...")
                transformOrigin: Item.Right
                Layout.fillWidth: true
            }
        }

        RowLayout {
            Layout.fillWidth: true
            Text {
                text: qsTr("Cci:")
                textFormat: Text.PlainText
                font.pixelSize: 12
                verticalAlignment: Text.AlignVCenter
                transformOrigin: Item.Left
            }
            TextField {
                id: textCci
                text: qsTr("Cci...")
                transformOrigin: Item.Right
                Layout.fillWidth: true
            }
        }

        RowLayout {
            Layout.fillWidth: true
            Text {
                text: qsTr("Subject:")
                textFormat: Text.PlainText
                font.pixelSize: 12
                verticalAlignment: Text.AlignVCenter
                transformOrigin: Item.Left
            }
            TextField {
                id: textSubject
                text: qsTr("Subject...")
                transformOrigin: Item.Right
                Layout.fillWidth: true
            }
        }

        ColumnLayout {
            Layout.fillWidth: true
            TextArea {
                id: msgArea
                text: qsTr("Email sent with PyMailDev.")
                Layout.fillHeight: true
                Layout.fillWidth: true
                //textFormat: Qt.RichText
            }
        }

        RowLayout {
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
            Layout.fillWidth: true
            TextArea {
                id: logArea
                text: qsTr("Log Area")
                enabled: false
                Layout.fillHeight: true
                Layout.fillWidth: true
                //textFormat: Qt.RichText
            }
        }
    }
}
