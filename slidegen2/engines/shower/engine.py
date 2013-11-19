# *-* coding=utf-8 *-*
from slidegen2.engines.common_commands import title, author
from slidegen2.engines.common_commands import math as cmd_math
from slidegen2.iengine import IEngine
from slidegen2.text_formatters import markdown_formatter
from slidegen2.util import get_formatter, get_text_formatter
#from slidegen2.engines.shower.commands import all_command

__author__ = 'reyoung'


class ShowerEngine(IEngine):
    def __init__(self):
        IEngine.__init__(self)
        self.__context = {}

    def begin_process(self, *args, **kwargs):
        print "Begin Process"
        self.__context.clear()

    def process(self):
        IEngine.process(self, context=self.__context)

    @staticmethod
    def instance(config):
        fmt = get_formatter(config)
        eng = ShowerEngine()
        eng.set_document_formatter(fmt)
        fmt = get_text_formatter(config)
        if fmt is None:
            fmt = markdown_formatter
        eng.set_text_formatter(fmt)
        eng.add_command(author)
        eng.add_command(title)
        eng.add_command(cmd_math)
        return eng


if __name__ == "__main__":
    test_data = """
$title: |
     *Title Of Slide*
---
$author:
  name: reyoung
  email: reyoung@126.com
---
$math: |
    true
"""
    eng = ShowerEngine.instance({"content": test_data})
    eng.process()
    #print eng.__context