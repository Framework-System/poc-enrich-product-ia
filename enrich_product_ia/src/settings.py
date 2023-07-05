import logging.config
import os

from dotenv import load_dotenv


load_dotenv()


# Directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = f"{BASE_DIR}/templates"


# OpenAI settings
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "text-davinci-003")
OPENAI_TEMPERATURE = int(os.getenv("OPENAI_TEMPERATURE", 0))
OPENAI_MAX_TOKENS = int(os.getenv("OPENAI_MAX_TOKENS", 1000))


# Logs settings
LOGS_LEVEL = os.getenv("LOGS_LEVEL", "INFO")

BASE_LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "detailed": {
            "()": "colorlog.ColoredFormatter",
            "format": (
                "%(asctime)s | %(bold)s%(name)s%(reset)s | %(blue)s%(funcName)s | "
                "L%(lineno)s | %(log_color)s%(levelname)s%(reset)s | %(message)s"
            ),
        }
    },
    "filters": {},
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "detailed",
            "filters": [],
        },
    },
    "loggers": {},
    "root": {
        "level": LOGS_LEVEL,
        "handlers": ["console"]
    },
}

logging.config.dictConfig(BASE_LOGGING_CONFIG)
