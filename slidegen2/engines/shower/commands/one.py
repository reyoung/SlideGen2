from slidegen2.engines.shower.commands import slide
from jinja2 import Template
import cgi

__author__ = 'reyoung'


def get_key():
    return "one"


def default_converter(item, text_formatter):
    """
    @param item:
    @param text_formatter: a text formatter
    @return:
    """
    return text_formatter.process(item.__str__())


def convert_content(content, text_formatter):
    if content is None:
        return ""
    elif isinstance(content, list):
        retv = ""
        for c in content:
            if isinstance(c, dict):
                for k in c:
                    cvt = converters.get(k, default_converter)
                    retv += cvt(c[k], text_formatter)
                    retv += "\n"
        return retv


def process(params, context, text_formatter, *args, **kwargs):
    """
    Process One Slide
    @param params:
    @param context:
    @param args:
    @param kwargs:
    @return: None
    @type params: dict
    @type context: dict
    """
    title = params.get("title", None)
    footer = params.get("footer", title)
    content = params.get("content", None)
    _id = params.get("id", None)
    tpl_str = """
{% if title is not none %}
<h2>{{ title }}</h2>
{% endif %}
{{ content }}
{% if footer is not none %}
<footer>{{ footer }}</footer>
{% endif %}
"""
    tpl = Template(tpl_str)
    p = dict()
    p["id"] = _id
    p["content"] = tpl.render(
        title=title,
        footer=footer,
        content=convert_content(content, text_formatter)
    )
    slide.process(params=p, context=context, text_formatter=text_formatter, *args, **kwargs)


def get_next_mark(item):
    mark_next = item.get("next", False)
    if isinstance(mark_next, str):
        mark_next = mark_next == "true" or mark_next == "True"
    return mark_next


def quote(item, text_formatter):
    author = None
    #content = None
    mark_next = False
    if isinstance(item, dict):
        content = item.get("content", None)
        author = item.get("author", None)
        mark_next = get_next_mark(item)
    else:
        content = item.__str__()
    tpl_str = """
<figure {% if mark_next %} class="next" {% endif %}>
    <blockquote>
        {{ content }}
    </blockquote>
    {% if author is not none %}
    <figcaption>{{ author }}</figcaption>
    {% endif %}
</figure>
    """
    tpl = Template(tpl_str)
    return tpl.render(content=text_formatter.process(content), author=text_formatter.process(author),
                      mark_next=mark_next)


def remove_p(content):
    _p = "<p>"
    _np = "</p>"
    if content.startswith(_p) and content.endswith(_np):
        content = content[len(_p):-len(_np)]
    return content


def p(item, text_formatter):
    if isinstance(item, dict):
        content = item.get("content", "")
        next_mark = get_next_mark(item)
        content = text_formatter.process(content)
        content = remove_p(content)
        tpl_str = """
<p {% if next_mark %} class="next" {% endif %}>{{ content }}</p>
        """
        tpl = Template(tpl_str)
        return tpl.render(content=content, next_mark=next_mark)
    else:
        return default_converter(item, text_formatter)


def ul(item, text_formatter, **kwargs):
    next_mark = False
    if isinstance(item, dict):
        content = item.get("content", list())
        next_mark = get_next_mark(item)
    elif isinstance(item, list):
        content = item
    else:
        content = None
    if content is not None:
        list_markup = kwargs.get("list_markup", "ul")
        tpl_str = """
<{{list_markup}}>
    {% for item in content %}
    <li {% if next_mark %} class="next" {% endif %}>{{item}}</li>
    {% endfor %}
</{{list_markup}}>
"""
        tpl = Template(tpl_str)

        def process_item(x):
            if isinstance(x, dict):
                k = x.keys()[0]
                v = x[k]
                k = remove_p(text_formatter.process(k))
                _tpl_str = """{{ k }} {{ content }}"""
                _tpl = Template(_tpl_str)
                if isinstance(v, list):
                    _content = ul(v, text_formatter, list_markup=list_markup)
                elif isinstance(v, dict):
                    _type = v.get('type', list_markup)
                    _content = ul(v.get('content', None), text_formatter, list_markup=_type)
                else:
                    _content = ""
                return _tpl.render(k=k, content=_content)
            else:
                return remove_p(text_formatter.process(x))

        new_list = map(process_item, content)
        return tpl.render(list_markup=list_markup, next_mark=next_mark, content=new_list)
    else:
        return ""


def code(item, *args, **kwargs):
    ln = False
    next_mark = False
    if isinstance(item, basestring):
        content = item
    elif isinstance(item, dict):
        content = item.get("content", None)
        ln = item.get("line_number", False)
        if isinstance(ln, basestring):
            ln = ln == "True" or ln == "true"
        next_mark = get_next_mark(item)
    else:
        content = None
    if content is None:
        return ""
    else:
        tpl_str = """
<pre {% if next_mark %}class="next"{% endif %}><code>{{ content }}</code></pre>
        """
        content = cgi.escape(content)
        if not ln:
            __tpl = Template(tpl_str)
            return __tpl.render(content=content, next_mark=next_mark)
        else:
            content = content.split('\n')[:-1]
            tpl_str = """
<pre {% if next_mark %}class="next"{% endif %}>{% for line in content %}<code>{{ line }}</code>
{% endfor %}</pre>
"""
            __tpl = Template(tpl_str)
            return __tpl.render(content=content,next_mark=next_mark)


converters = {
    "quote": quote,
    "p": p,
    "ul": ul,
    "ol": lambda x, y: ul(x, y, list_markup="ol"),
    "code": code
}

