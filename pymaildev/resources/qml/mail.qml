import QtQuick 2.4
import QtQuick.Controls.Universal 2.0
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles.Desktop 1.0

ApplicationWindow {
    title: qsTr("Composition mail")
    width: 800
    height: 600
    menuBar: MenuBar {
        Menu {
            title: qsTr("&Fichier")
            MenuItem {
                text: qsTr("Sauvgarder")
                onTriggered: console.log("menu item clicked")
                enabled: false
            }
        }
    }
    MailForm {
        anchors.margins: 6
        anchors.fill: parent
    }
    statusBar: StatusBar {
        Label { text: "..." }
    }
}
