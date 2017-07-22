import QtQuick 2.0
import QtQuick.Controls 1.4

TextField {
    placeholderText: qsTr("adr@domain.com")
    inputMethodHints: Qt.ImhNoAutoUppercase | Qt.ImhEmailCharactersOnly // | Qt.ImhNoPredictiveText
    validator: RegExpValidator { regExp: /(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)/ }
}
