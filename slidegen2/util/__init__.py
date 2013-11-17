from slidegen2.document_formatters.yaml_formatter import YAMLFormatter
from slidegen2.text_formatters import markdown_formatter

__author__ = 'reyoung'


def get_formatter(config):
    """
    Get Document Formatter By Config
    @param config:
    @return: Document Formatter
    @type config: dict
    """
    fn = config.get("fn")
    if fn is None:
        fn = config.get("filename")

    content = config.get("content")

    if fn is not None or content is not None:
        return YAMLFormatter(fn=fn, content=content)
    else:
        return config.get("document_formatter")


def get_text_formatter_method(text_formatter):
    if text_formatter is not None:
        return text_formatter.process
    else:
        return lambda x: x


def get_text_formatter(config):
    if "text_formatter" in config:
        if config["text_formatter"] == "markdown" or config["text_formatter"] == "md":
            return markdown_formatter
    else:
        return None