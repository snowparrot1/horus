#!/usr/bin/python
# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------#
#                                                                       #
# This file is part of the Horus Project                                #
#                                                                       #
# Copyright (C) 2014 Mundo Reader S.L.                                  #
#                                                                       #
# Date: June 2014                                                       #
# Author: Jesús Arroyo Torrens <jesus.arroyo@bq.com>                    #
#                                                                       #
# This program is free software: you can redistribute it and/or modify  #
# it under the terms of the GNU General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or     #
# (at your option) any later version.                                   #
#                                                                       #
# This program is distributed in the hope that it will be useful,       #
# but WITHOUT ANY WARRANTY; without even the implied warranty of        #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the          #
# GNU General Public License for more details.                          #
#                                                                       #
# You should have received a copy of the GNU General Public License     #
# along with this program. If not, see <http://www.gnu.org/licenses/>.  #
#                                                                       #
#-----------------------------------------------------------------------#

from horus.gui.util.workbench import *

from horus.util import resources

class CalibrationWorkbench(Workbench):

	def __init__(self, parent):
		Workbench.__init__(self, parent)

		self.load()

	def load(self):

		self._toolbar.AddLabelTool(wx.ID_EXIT, '', wx.Bitmap(resources.getPathForImage("load.png")))
		self._toolbar.Realize()

		self._leftPanel = self.getLeftPanel()
		wx.StaticText(self._leftPanel, -1, "Calibration")

		self._rightPanel.SetBackgroundColour(wx.GREEN)
