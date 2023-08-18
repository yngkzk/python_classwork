import sys


class Levels:
    ERROR = 0
    WARNING = 1
    INFO = 2
    DEBUG = 3
    TRACE = 4
    names = ("[E] ", "[W] ", "[I] ", "[D] ", "[T] ")


def _log(level, *args, **kwargs):
    if level >= len(Levels.names):
        return
    if level > current_log_level:
        return
    print(Levels.names[level], *args, **kwargs)


def logE(*args, **kwargs):
    _log(Levels.ERROR, *args, **kwargs)


def logW(*args, **kwargs):
    _log(Levels.WARNING, *args, **kwargs)


def logI(*args, **kwargs):
    _log(Levels.INFO, *args, **kwargs)


def logD(*args, **kwargs):
    _log(Levels.DEBUG, *args, **kwargs)


def logT(*args, **kwargs):
    _log(Levels.TRACE, *args, **kwargs)


current_log_level = Levels.TRACE
if __name__ == "__main__":
    print(sys.argv)
    if '--level' in sys.argv:
        index = sys.argv.index('--level')
        desired_level = sys.argv[index+1]
        if desired_level == 'debug':
            current_log_level = Levels.DEBUG
        elif desired_level == 'info':
            current_log_level = Levels.INFO
        elif desired_level == 'warning':
            current_log_level = Levels.WARNING
        elif desired_level == 'trace':
            current_log_level = Levels.TRACE
        elif desired_level == 'error':
            current_log_level = Levels.ERROR

    logI(Levels.INFO, "New client has joined. id = ", 32324555)
    logE(Levels.ERROR, "Error: Don't have access to the server. ", "192.102.52.84")
    logT(Levels.TRACE, "main() called.")
    logW(Levels.WARNING, "Your password is not good enough", "****")
    logD(Levels.DEBUG, "This is debug message")
