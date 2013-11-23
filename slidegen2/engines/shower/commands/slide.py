from jinja2 import Template
from slidegen2.engines.shower.commands import insert_result_into_context

__author__ = 'reyoung'


def get_key():
    return "slide"


def process(params, context, text_formatter, *args, **kwargs):
    if isinstance(params, dict):
        tplStr = """
<section class="slide" {% if id is not none %} id="{{ id }}" {% endif %}>
<div>{{ content }}</div>
</section>
"""
        need_escape = params.get("need_escape", "false")
        if need_escape == "true" or need_escape is True:
            content = params.get("content", "")
            content = text_formatter.process(content)
            params["content"] = content
        tpl = Template(tplStr)
        rst = tpl.render(**params)
        insert_result_into_context(context, rst)