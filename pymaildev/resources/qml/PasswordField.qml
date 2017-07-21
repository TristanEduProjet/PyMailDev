import QtQuick 2.2
import QtQuick.Controls 1.4

TextField {
    inputMethodHints: Qt.ImhNoAutoUppercase | Qt.ImhNoPredictiveText | Qt.ImhSensitiveData
    placeholderText: qsTr("pswd")
    echoMode: TextInput.Password
}
