# coding=utf-8
"""DockWidget test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'notYet@bruh.mp'
__date__ = '2019-03-20'
__copyright__ = 'Copyright 2019, Fantastic Four .group'

import unittest

from PyQt5.QtGui import QDockWidget

from election_plugin_dockwidget import Fantastic_Group_ProjectDockWidget

from utilities import get_qgis_app

QGIS_APP = get_qgis_app()


class Fantastic_Group_ProjectDockWidgetTest(unittest.TestCase):
    """Test dockwidget works."""

    def setUp(self):
        """Runs before each test."""
        self.dockwidget = Fantastic_Group_ProjectDockWidget(None)

    def tearDown(self):
        """Runs after each test."""
        self.dockwidget = None

    def test_dockwidget_ok(self):
        """Test we can click OK."""
        pass

if __name__ == "__main__":
    suite = unittest.makeSuite(Fantastic_Group_ProjectDialogTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

