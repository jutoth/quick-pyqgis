# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QuickPyQGIS
                                 A QGIS plugin
 QuickPyQGIS is a QGIS plugin that streamlines PyQGIS scripting by generating ready-to-use code snippets directly within the QGIS interface. With actions integrated into the UI, it allows users to quickly populate the Python Console with relevant PyQGIS code, enhancing productivity and simplifying script development.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2024-09-02
        git sha              : $Format:%H$
        copyright            : (C) 2024 by Julius Tóth
        email                : juliustoth1996@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.core import QgsMapLayer
from qgis.gui import QgisInterface
from qgis.utils import iface
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction



from .utils.code_snippet_factory import generate_snippet_get_map_layer, generate_snippet_create_map_layer


class QuickPyQGIS:

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        self.iface: QgisInterface = iface
        self.plugin_dir = os.path.dirname(__file__)
        
        self.action_get_maplayer = None
        self.action_create_maplayer = None

        self.actions = []
        self.menu = '&QuickPyQGIS'
        self.ltv = iface.layerTreeView()



    def add_action(self, icon_path, text, callback, enabled_flag=True, add_to_menu=True, 
                   add_to_toolbar=True, status_tip=None, whats_this=None, parent=None):

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/quick-pyqgis/resources/icon.png'
        self.add_action(
            icon_path,
            text=u'QuickPyQGIS',
            callback=self.run,
            parent=self.iface.mainWindow())

        
        # self.ltv.contextMenuAboutToShow.connect(add_action_layer_context_menu)
        self.action_get_maplayer = QAction('mapLayersByName')
        self.action_get_maplayer.triggered.connect(generate_snippet_get_map_layer)

        self.action_create_maplayer = QAction('Create QgsVectorLayer')
        self.action_create_maplayer.triggered.connect(generate_snippet_create_map_layer)

        self.iface.addCustomActionForLayerType(self.action_get_maplayer, 'Generate Code Snippet', QgsMapLayer.VectorLayer, True)
        self.iface.addCustomActionForLayerType(self.action_create_maplayer, 'Generate Code Snippet', QgsMapLayer.VectorLayer, True)



    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                u'&QuickPyQGIS',
                action)
            self.iface.removeToolBarIcon(action)
            
        # self.ltv.contextMenuAboutToShow.disconnect(add_action_layer_context_menu)
        self.iface.removeCustomActionForLayerType(self.action_get_maplayer)
        self.iface.removeCustomActionForLayerType(self.action_create_maplayer)

    def run(self):
        ...
