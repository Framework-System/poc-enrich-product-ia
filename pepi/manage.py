import sys

from services.openai import OpenAI
from utils.templates import get_template_content


if __name__ == "__main__":
    prompt = "Say this is a test"

    if "--template" in sys.argv:
        kwargs = {}
        template_name = sys.argv[sys.argv.index("--template") + 1]

        if "--ean" in sys.argv:
            ean_code = sys.argv[sys.argv.index("--ean") + 1]
            kwargs["ean_code"] = ean_code

        if "--name" in sys.argv:
            ean_code = sys.argv[sys.argv.index("--name") + 1]
            kwargs["name"] = ean_code

        prompt = get_template_content(template_name, **kwargs)

    elif "--prompt" in sys.argv:
        prompt = sys.argv[sys.argv.index("--prompt") + 1]

    openai = OpenAI()
    openai.question(prompt, json_format=False)
