import QtQuick 2.4
import QtQuick.Controls.Universal 2.0
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles.Desktop 1.0
import QtQuick.Layouts 1.3

ApplicationWindow {
    title: qsTr("Mail composer")
    width: 800
    height: 600
    id: window
    menuBar: MenuBar {
        Menu {
            title: qsTr("&File")
            MenuItem {
                text: qsTr("Save")
                iconSource: "../icons/16x16/Save.png"
                onTriggered: console.log("menu item clicked")
                shortcut: StandardKey.Save
                enabled: false
            }
            MenuSeparator {}
            MenuItem {
                text: qsTr("Exit")
                iconSource: "../icons/16x16/Exit.png"
                onTriggered: window.close()
                shortcut: StandardKey.Quit
            }
        }
        Menu {
            title: qsTr("&Edit")
            MenuItem {
                action: undoAction
                iconSource: "../icons/16x16/Undo.png"
            }
            MenuItem {
                action: redoAction
                iconSource: "../icons/16x16/Redo.png"
            }
            MenuSeparator {}
            MenuItem {
                action: cutAction
                iconSource: "../icons/16x16/Cut.png"
            }
            MenuItem {
                action: copyAction
                iconSource: "../icons/16x16/Copy.png"
            }
            MenuItem {
                action: pasteAction
                iconSource: "../icons/16x16/Paste.png"
            }
        }
    }

    toolBar: ToolBar {
        RowLayout {
            Layout.fillWidth: true
            ToolButton {
                action: undoAction
                iconSource: "../icons/24x24/Undo.png"
            }
            ToolButton {
                action: undoAction
                iconSource: "../icons/24x24/Redo.png"
            }
            ToolBarSeparator {}
            ToolButton {
                action: cutAction
                iconSource: "../icons/24x24/Cut.png"
            }
            ToolButton {
                action: copyAction
                iconSource: "../icons/24x24/Copy.png"
            }
            ToolButton {
                action: pasteAction
                iconSource: "../icons/24x24/Paste.png"
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

    Action {
        id: cutAction
        text: qsTr("Cut")
        shortcut: StandardKey.Cut
        //onTriggered:
        //iconName: "edit-cut"
        iconName: "Cut"
        enabled: false
    }
    Action {
        id: copyAction
        text: qsTr("Copy")
        shortcut: StandardKey.Copy
        //onTriggered:
        //iconName: "edit-copy"
        iconName: "Copy"
        enabled: false
    }
    Action {
        id: pasteAction
        text: qsTr("Paste")
        shortcut: StandardKey.Paste
        //onTriggered:
        //iconName: "edit-paste"
        iconName: "Paste"
        enabled: false
    }
    Action {
        id: undoAction
        text: qsTr("Undo")
        shortcut: StandardKey.Undo
        //onTriggered:
        iconName: "Undo"
        enabled: false
    }
    Action {
        id: redoAction
        text: qsTr("Redo")
        shortcut: StandardKey.Redo
        //onTriggered:
        iconName: "Redo"
        enabled: false
    }
}
