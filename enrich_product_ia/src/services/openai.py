import logging.config
import json
import openai

from .. import settings

logger = logging.getLogger(__name__)


class OpenAI:
    def __init__(self):
        self.__api_key = settings.OPENAI_API_KEY
        openai.api_key = self.__api_key

        self.model = settings.OPENAI_MODEL
        self.temperature = settings.OPENAI_TEMPERATURE
        self.max_tokens = settings.OPENAI_MAX_TOKENS

    def question(self, prompt: str, json_format=False):
        logger.info(f"prompt:\n{prompt}\n")

        try:
            response = openai.Completion.create(
                model=self.model,
                prompt=prompt,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
            ).choices[0].text
        except Exception as e:
            logger.error(e)
            raise

        logger.info(f"response:\n{response}\n")

        if json_format:
            response = json.loads(response)

        return response
