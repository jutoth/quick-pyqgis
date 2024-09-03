from qgis.core import (QgsApplication, 
                       Qgis, 
                       QgsVectorLayer, 
                       QgsFeature, 
                       QgsGeometry,
                       QgsField)

from qgis.utils import iface


def generate_snippet_get_map_layer():
    layer_name = iface.activeLayer().name()
    code_snippet = f"QgsProject.instance().mapLayersByName('{layer_name}')[0]"
    code_snippet_to_clipboard(code_snippet)



def generate_snippet_create_map_layer():
    layer:QgsVectorLayer = iface.activeLayer()
    layer_name = layer.name() + '_copy'
    fields = layer.fields()

    snippet_declare_layer = f"layer = QgsVectorLayer('', '{layer_name}', 'memory')\n\n"

    snippet_attribute_values = 'feature_attributes = [\n' + 4 * ' '

    snippet_wkt_geometries = 'feature_geometries = [\n' + 4 * ' '
    n_features = layer.featureCount()
    for i, feature in enumerate(layer.getFeatures()):
        attribute_values, wkt_geometry = generate_snippet_feature(feature, fields, i, n_features)
        snippet_attribute_values += attribute_values
        snippet_wkt_geometries += wkt_geometry

    code_snippet = snippet_declare_layer + snippet_attribute_values + snippet_wkt_geometries
    code_snippet_to_clipboard(code_snippet)


def generate_fields_declaration(layer: QgsVectorLayer):
    ...

def generate_snippet_feature(feature: QgsFeature, fields, feature_index, n_features) -> tuple[str]:
    feature_attributes_string = '['
    for i, field in enumerate(fields):
        typeName = field.typeName()
        attribute_value = feature.attribute(field.name())
        feature_geometry_wkt_string = f"'{feature.geometry().asWkt()}'"
        if typeName in ['String']:
            attribute_value = f"'{attribute_value}'"
        feature_attributes_string += f'{attribute_value}'
        if i + 1 != fields.count():
            feature_attributes_string += ', '
    if feature_index + 1 < n_features:
        feature_attributes_string += "]" + ",\n" + 4 * ' '
        feature_geometry_wkt_string += ",\n" + 4 * ' '
    else:
        feature_attributes_string += "]\n]" + '\n\n'
        feature_geometry_wkt_string += '\n' + ']' + '\n\n'

    return feature_attributes_string, feature_geometry_wkt_string



def code_snippet_to_clipboard(code_snippet) -> None:
    app = QgsApplication.instance()
    clipboard = app.clipboard()
    clipboard.setText(code_snippet)
    iface.messageBar().pushMessage("Info", "Code snippet added to clipboard", level=Qgis.Info, duration=3)

