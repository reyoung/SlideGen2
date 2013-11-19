import sys

__author__ = 'reyoung'


class ICommand(object):
    def __init__(self):
        pass

    @staticmethod
    def get_key():
        """
        @type return: str
        """
        return None

    @staticmethod
    def process(*args, **kwargs):
        """
        @type return: str
        """
        return ""


class IEngine(object):
    def __init__(self):
        self.__commands = {}
        self.__document_formatter = None
        self.__text_formatter = None

    def add_command(self, cmd):
        """
        @param cmd: add slide engine command
        @return:
        """
        self.__commands[cmd.get_key()] = cmd

    def set_document_formatter(self, fmt):
        """
        @param fmt: the document format
        @type fmt: IDocumentFormatter
        @return: True if success
        """
        if isinstance(fmt, IDocumentFormatter):
            self.__document_formatter = fmt
            return True
        else:
            return False

    def set_text_formatter(self, fmt):
        """
        @param fmt: the text formatter
        @type fmt: ITextFormatter
        @return: None
        """
        if hasattr(fmt, "process") and callable(getattr(fmt, "process")):
            self.__text_formatter = fmt
            return True
        else:
            return False

    @staticmethod
    def instance(config):
        return None

    def process(self, *args, **kwargs):
        self.begin_process(text_formatter=self.__text_formatter, *args, **kwargs)
        iter = self.__document_formatter.get_command_iterator(text_formatter=self.__text_formatter, *args, **kwargs)
        for key, params in iter:
            if key is None:
                break
            else:
                cmd = self.__commands.get(key)
                if cmd is not None:
                    self.handle_result(
                        cmd.process(params=params, text_formatter=self.__text_formatter, *args, **kwargs))
                else:
                    self.no_such_command(key)

        return self.end_process(text_formatter=self.__text_formatter, *args, **kwargs)

    def begin_process(self, *args, **kwargs):
        pass

    def end_process(self, *args, **kwargs):
        pass

    def handle_result(self, result):
        pass

    @staticmethod
    def no_such_command(key):
        print "There is no such command with key '%s' in this engine" % key
        sys.exit(1)


class IDocumentFormatter(object):
    def __init__(self):
        pass

    def get_command_iterator(self, *args, **kwargs):
        pass


class ITextFormatter(object):
    @staticmethod
    def process(text):
        return ""