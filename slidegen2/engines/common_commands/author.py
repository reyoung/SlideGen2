from slidegen2.util import get_text_formatter_method, command_type_mismatch

__author__ = 'reyoung'


def get_key():
    return "$author"

def process(params, context, text_formatter, *args, **kwargs):
    """
    Process Author Command of shower
    @param params: auther name, or email
    @param context: engine context
    @param text_formatter: formatter
    @param args:
    @param kwargs:
    @return:
    @type context:dict
    """
    fmt = get_text_formatter_method(text_formatter)
    if isinstance(params, str):
        context['author'] = fmt(params)
    elif isinstance(params, dict):
        author = params.get("name", None)
        email = params.get("email", None)
        if author is not None:
            context['author'] = fmt(author)
        if email is not None:
            context['email'] = fmt(author)
    else:
        command_type_mismatch(params)