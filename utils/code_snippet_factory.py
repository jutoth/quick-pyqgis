from qgis.core import QgsApplication, Qgis
from qgis.utils import iface


def generate_snippet_get_map_layer():
    layer_name = iface.activeLayer().name()
    code_snippet = f"QgsProject.instance().mapLayersByName('{layer_name}')[0]"
    code_snippet_to_clipboard(code_snippet)


def code_snippet_to_clipboard(code_snippet):
    app = QgsApplication.instance()
    clipboard = app.clipboard()
    clipboard.setText(code_snippet)
    iface.messageBar().pushMessage("Info", "Code snippet added to clipboard", level=Qgis.Info, duration=3)

