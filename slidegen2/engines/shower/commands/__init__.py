__author__ = 'reyoung'


def insert_result_into_context(context, rst):
    result = context.get("result", "")
    result = """%s
%s""" % (result, rst)
    context["result"] = result