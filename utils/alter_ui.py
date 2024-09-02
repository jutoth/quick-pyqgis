from PyQt5.QtWidgets import QMenu, QAction
from qgis.core import QgsMapLayer
from qgis.gui import QgsLayerTreeViewMenuProvider
from qgis.utils import iface

from .code_snippet_factory import *

def add_action_layer_context_menu(menu: QMenu) -> None:
    menu.addSeparator()
    menu.addAction('Code Snippet: get mapLayer', generate_snippet_get_map_layer)