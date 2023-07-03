import unicodedata


def strip_accents(content: str) -> str:
   return "".join(
      character for character in unicodedata.normalize("NFD", content)
      if unicodedata.category(character) != "Mn"
   )
