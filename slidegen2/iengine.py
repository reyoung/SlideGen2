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

    def add_command(self, cmd):
        """
        @param cmd: add slide engine command
        @type cmd: ICommand
        @return:
        """
        self.__commands[cmd.get_key()] = cmd

    @staticmethod
    def instance(config):
        return None

    def process(self, *args, **kwargs):
        self.begin_process(*args, **kwargs)
        while True:
            key, params = self.get_next_command(*args, **kwargs)
            if key is None:
                break
            else:
                cmd = self.__commands[key]
                self.handle_result(cmd.process(params = params, *args,**kwargs))

        return self.end_process(*args, **kwargs)

    def begin_process(self, *args, **kwargs):
        pass

    def end_process(self, *args, **kwargs):
        pass

    def handle_result(self, result):
        pass
