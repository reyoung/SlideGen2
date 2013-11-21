from slidegen2.util import command_type_mismatch

__author__ = 'reyoung'


def get_key():
    return "$author"

def process(params, context, *args, **kwargs):
    """
    Process Author Command of shower
    @param params: auther name, or email
    @param context: engine context
    @param args:
    @param kwargs:
    @return:
    @type context:dict
    """
    if isinstance(params, str):
        context['author'] = params
    elif isinstance(params, dict):
        author = params.get("name", None)
        email = params.get("email", None)
        if author is not None:
            context['author'] = author
        if email is not None:
            context['email'] = email
    else:
        command_type_mismatch(params)