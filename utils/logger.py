import logging
import colorama
from colorama import Fore, Style

# Initialize colorama for cross-platform terminal coloring
colorama.init()

# Define color mappings
COLORS = {
    "debug": Fore.GREEN,
    "info": Fore.BLUE,
    "warning": Fore.YELLOW,
    "error": Fore.RED,
    "critical": Fore.RED,
}


class ColoredFormatter(logging.Formatter):
    """A custom formatter that adds colors to log messages"""

    def format(self, record):
        # Set the message color based on the log level
        message_color = COLORS.get(record.levelname.lower(), "")

        # Reset color at the end of the message
        message = super().format(record)
        message += Style.RESET_ALL

        # Apply color to the message
        formatted_message = message_color + message

        return formatted_message


class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # Create console handler and set the log level to DEBUG
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # Create formatter and add it to the console handler
        formatter = ColoredFormatter(
            "[%(asctime)s] %(levelname)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )
        console_handler.setFormatter(formatter)

        # Add the console handler to the logger
        self.logger.addHandler(console_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
