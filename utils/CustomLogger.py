import logging
import logging.config


class CustomLogger:
    def __init__(self):
        self.log = logging.config
        self.log.fileConfig(r'D:\LearnPlatform\automation-with-python\utils\logging.conf')
        self.logger = logging.getLogger('selenium')

    def write_message_info(self, message):
        self.logger.info(f"{message}".format(message=message))

    def write_message_debug(self, message):
        self.logger.debug(f"{message}".format(message=message))

    def write_message_warning(self, message):
        self.logger.warning(f"{message}".format(message=message))

    def write_message_critical(self, message):
        self.logger.critical(f"{message}".format(message=message))

    def write_message_error(self, message):
        self.logger.error(f"{message}".format(message=message))
