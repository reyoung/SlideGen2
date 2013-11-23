from markdown import Markdown

__author__ = 'reyoung'

md = Markdown()


def process(text):
    """
    Process Text To Markdown
    @param text: original text
    @type text: str
    @return: markdown str
    """
    if isinstance(text, str) or isinstance(text, unicode):
        return md.convert(text)
    elif isinstance(text, int) or isinstance(text, float):
        return md.convert(str(text))
    else:
        return text


if __name__ == "__main__":
    print process("*text*")