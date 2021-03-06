import os

if os.environ.get('QGIS_PLUGIN_USE_DEBUGGER') == 'pydevd':
    try:
        import pydevd

        pydevd.settrace('localhost', port=5678, stdoutToServer=True, stderrToServer=True)
    except Exception as e:
        print('Unable to create pydevd debugger: {}'.format(e))


def classFactory(iface):
    from .kunta_gml_loader_plugin import KuntagmlLoader
    return KuntagmlLoader(iface)
