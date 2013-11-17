from yaml import load_all

try:
    from yaml import CLoader as Loader
except ImportError:
    print("Using pure python YAML loader, it may be slow.")
    from yaml import Loader
from iengine import IDocumentFormatter

__author__ = 'reyoung'


class YAMLFormatter(IDocumentFormatter):
    def __init__(self, fn=None, content=None):
        IDocumentFormatter.__init__(self)
        if fn is not None:
            with file(fn, "r") as f:
                self.__content = load_all(f, Loader=Loader)
        else:
            self.__content = load_all(content, Loader=Loader)

    def get_command_iterator(self, *args, **kwargs):
        for item in self.__content:
            yield YAMLFormatter.__process_item(item)

    @staticmethod
    def __process_item(item):
        if isinstance(item, dict) and len(item) == 1:
            key = item.iterkeys().__iter__().next()
            value = item[key]
            return key, value

