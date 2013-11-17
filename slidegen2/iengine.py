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
        self.__document_format = None

    def add_command(self, cmd):
        """
        @param cmd: add slide engine command
        @type cmd: ICommand
        @return:
        """
        self.__commands[cmd.get_key()] = cmd

    def set_document_format(self, fmt):
        """
        @param fmt: the document format
        @type fmt: IDocumentFormatter
        @return: None
        """
        self.__document_format = fmt

    @staticmethod
    def instance(config):
        return None

    def process(self, *args, **kwargs):
        self.begin_process(*args, **kwargs)
        iter = self.__document_format.get_command_iterator(*args,**kwargs)
        for key,params in iter:
            if key is None:
                break
            else:
                cmd = self.__commands[key]
                self.handle_result(cmd.process(params=params, *args, **kwargs))

        return self.end_process(*args, **kwargs)

    def begin_process(self, *args, **kwargs):
        pass

    def end_process(self, *args, **kwargs):
        pass

    def handle_result(self, result):
        pass


class IDocumentFormatter(object):
    def __init__(self):
        pass

    def get_command_iterator(self, *args, **kwargs):
        pass