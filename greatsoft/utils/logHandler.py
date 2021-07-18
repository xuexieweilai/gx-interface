import logging
from pathlib import Path
import time


def get_timesuffix(timetag = "0"):
    if timetag == "0":
        return time.strftime('%y%m%d%H%M%S', time.localtime(time.time()))
    else:
        return timetag


class Logger(object):
    log_name = "gx-interface"
    log_path = Path(__file__).parent.parent /"logs"
    test_timestamp = "logger-default-timestamp"
    level = logging.DEBUG

    @ staticmethod
    def get_test_timestamp():
        return Logger.test_timestamp

    @ staticmethod
    def set_log_level(l):
        Logger.level = l

    def __init__(self, name):
        self._name = name
        if not Logger.log_path.exists():
            Logger.log_path.mkdir()
        if Logger.test_timestamp == "logger-default-timestamp":
            Logger.test_timestamp = get_timesuffix()
        self._log_path = Logger.log_path / (Logger.log_name + "_" + Logger.test_timestamp)
        self._logger = logging.getLogger(name)
        self._logger.setLevel(Logger.level)

        formatter = logging.Formatter('%(asctime)s [%(name)s][%(levelname)s]: %(message)s')
        file_handler = logging.FileHandler(self._log_path)
        file_handler.setLevel(Logger.level)
        file_handler.setFormatter(formatter)
        self._logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(Logger.level)
        stream_handler.setFormatter(formatter)
        self._logger.addHandler(stream_handler)

    def debug(self, msg, *args, **kwargs):
        self._logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self._logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self._logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self._logger.error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        self._logger.info(msg, *args, **kwargs)




# if __name__ == "__main__":
#     Logger("测试log").info("测试logger")