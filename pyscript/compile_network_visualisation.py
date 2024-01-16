@service
def compile_network_visualisation():
    '''
    Wrapper for module to compile network visualisation.
    '''

    import sys

    if "/config/pyscript/modules" not in sys.path:
        sys.path.append("/config/pyscript/modules")

    from network_visualisation import network_visualisation
    network_visualisation()