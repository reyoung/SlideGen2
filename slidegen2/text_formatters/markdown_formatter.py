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
    return md.convert(text)


if __name__ == "__main__":
    print process("*text*")