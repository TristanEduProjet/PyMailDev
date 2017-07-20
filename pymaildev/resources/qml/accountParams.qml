import QtQuick 2.4
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles.Desktop 1.0
import QtQuick.Layouts 1.3

ApplicationWindow {
    width: 420
    height: 300
    title: qsTr("Account parameter")

    AccountParamsForm {
        anchors.fill: parent
        anchors.margins: 4
        Layout.fillHeight: true
        Layout.fillWidth: true
    }
}
