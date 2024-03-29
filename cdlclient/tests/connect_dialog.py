# -*- coding: utf-8 -*-
#
# Licensed under the terms of the BSD 3-Clause
# (see cdlclient/LICENSE for details)

"""
DataLab Remote client connection dialog example
"""

# guitest: show

from guidata.qthelpers import qt_app_context
from qtpy import QtWidgets as QW

from cdlclient import SimpleRemoteProxy
from cdlclient.widgets import ConnectionDialog


def test_dialog():
    """Test connection dialog"""
    proxy = SimpleRemoteProxy(autoconnect=False)
    with qt_app_context():
        dlg = ConnectionDialog(proxy.connect)
        if dlg.exec():
            QW.QMessageBox.information(None, "Connection", "Successfully connected")
        else:
            QW.QMessageBox.critical(None, "Connection", "Connection failed")


if __name__ == "__main__":
    test_dialog()
