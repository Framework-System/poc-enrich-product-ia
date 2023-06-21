import settings


def get_template_content(template_name: str, *args, **kwargs) -> str:
    template_content = None

    with open(f"{settings.TEMPLATES_DIR}/{template_name}", "r") as f:
        template_content = f.read()
        f.close()

    if kwargs:
        template_content = template_content.format(**kwargs)

    return template_content
