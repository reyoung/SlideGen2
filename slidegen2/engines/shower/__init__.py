from slidegen2.engines.shower.engine import ShowerEngine
__author__ = 'reyoung'





def instance(config):
    """
    New Instance of Shower SlideGen Engine
    @param config:
    @return: Shower SlideGen Engine
    @type config: dict
    """
    return ShowerEngine.instance(config)

