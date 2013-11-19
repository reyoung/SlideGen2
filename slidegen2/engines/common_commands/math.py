from slidegen2.util import get_text_formatter_method, str2bool, command_type_mismatch
import sys

__author__ = 'reyoung'


def get_key():
    return "$math"


def process(params, context, *args, **kwargs):
    enabled = False
    use_cdn = True
    if isinstance(params, str):
        enabled = str2bool(params),
    elif isinstance(params, dict):
        enabled = str2bool(params.get('enabled', ''))
        use_cdn = str2bool(params.get('use_cdn', 'true'))
    else:
        command_type_mismatch(params)
    context['math'] = {
        'enabled': enabled,
        'use_cdn': use_cdn
    }