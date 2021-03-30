KuntaGML QGIS Plugin
===================
![](https://github.com/GispoCoding/KuntaGML-QGIS-plugin/workflows/Tests/badge.svg)
![](https://github.com/GispoCoding/KuntaGML-QGIS-plugin/workflows/Release/badge.svg)

This QGIS3 plugin is developed for loading KuntaGML features directly from WFS API's. Inspired by these projects:
* [KuntaGMLPlugin](https://github.com/ernogispo/KuntaGMLPlugin)
* [gml_application_schema_toolbox](https://github.com/BRGM/gml_application_schema_toolbox)

This project utilizes [qgis_plugin_tools](https://github.com/GispoCoding/qgis_plugin_tools) submodule, so when cloning
the repository use `--recurse-submodules` in the following manner:
`git clone --recurse-submodules https://github.com/GispoCoding/KuntaGML-QGIS-plugin.git`

The plugin is still in beta-development. Please report issues preferably to Issues or to tuki@gispo.fi.

Developed by **Gispo Ltd**.

## Installation instructions

The QGIS plugin can be installed by downloading a release from this repository:

1. Download the latest release zip from GitHub releases [link](https://github.com/GispoCoding/KuntaGML-QGIS-plugin/releases).

2. Launch QGIS and navigate to the plugins menu by selecting Plugins - Manage and Install Plugins from the top menu.

3. Select the Install from ZIP tab, browse to the zip file you just downloaded, and click Install Plugin!

## Usage

![Plugin in action](/docs/k-gml.gif?raw=true "Plugin in action.")

## Licence

This plugin is licenced with [GNU Genereal Public License, version 3](https://www.gnu.org/licenses/gpl-3.0.en.html).