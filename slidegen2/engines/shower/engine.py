# *-* coding=utf-8 *-*
from slidegen2.engines.common_commands import title, author
from slidegen2.engines.common_commands import math as cmd_math
from slidegen2.engines.shower.commands import slide
from slidegen2.iengine import IEngine
from slidegen2.text_formatters import markdown_formatter
from slidegen2.util import get_formatter, get_text_formatter
from jinja2 import Template

__author__ = 'reyoung'


class ShowerEngine(IEngine):
    def __init__(self):
        IEngine.__init__(self)
        self.__context = {}

    def begin_process(self, *args, **kwargs):
        self.__context.clear()
        self.__context["engine_root"] = "shower"
        self.__context["theme_name"] = "bright"

    def process(self, output_param):
        return IEngine.process(self, context=self.__context, output_param=output_param)

    def end_process(self, output_param,*args, **kwargs):
        tpl = Template("""
<!DOCTYPE html>
<html>
<head>
    <title>{{ raw_title }}</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=680, user-scalable=no" />
    <meta http-equiv="x-ua-compatible" content="ie=edge" />
    <link rel="stylesheet" href="{{ engine_root }}/themes/{{theme_name}}/styles/screen.css" />
    {% if math is not none and math.enabled %}
        {% if math.use_cdn %}
        <script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
        {% endif %}
    {% endif %}
</head>
<body class="list">
    <header class="caption">
        <h1>{{ title }}</h1>
        {% if author is not none %}
        <h3>{{ author }}
            {% if email is not none %}
            &nbsp; E-Mail: {{ email }}
            {% endif %}
        </h3>
        {% endif %}
    </header>
    {{ result }}
    <div class="progress"><div></div></div>
    <script src="{{ engine_root }}/shower.js"></script>
</body>
</html>
""")
        if output_param['type'] == 'html':
            return tpl.render(**self.__context)

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
        eng.add_command(slide)
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
---
slide:
  id: 1
  content: |
     ## abc
  need_escape: true
"""
    eng = ShowerEngine.instance({"content": test_data})
    print eng.process({"type": "html"})
    #print eng.__context