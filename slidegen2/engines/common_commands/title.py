from slidegen2.iengine import ITextFormatter
from slidegen2.util import get_text_formatter_method

__author__ = 'reyoung'


def get_key():
    return "$title"


def process(params, context, text_formatter, *args, **kwargs):
    """
    Process Shower $title Command
    @param params: title String
    @param context: command context
    @type context: dict
    @param text_formatter: Text Formatter
    @type text_formatter: ITextFormatter
    @param args:
    @param kwargs:
    @return: None
    """
    fmt = get_text_formatter_method(text_formatter)
    if isinstance(params, str):
        context["title"] = fmt(params)
        context['raw_title']=params