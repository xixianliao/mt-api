from typing import Optional, Tuple

from app.constants import MODEL_TAG_SEPARATOR


def lowercaser(word: str) -> str:
    return word.lower()

def capitalizer(word: str) -> str:
    return word.capitalize()

def get_model_id(src: str, tgt: str, alt_id: Optional[str] = None) -> str:
    items = [src, tgt, alt_id] if alt_id else [src, tgt] 
    return MODEL_TAG_SEPARATOR.join(items)

def parse_model_id(model_id: str) -> Optional[Tuple[str, str, str]]:
    fields = model_id.split(MODEL_TAG_SEPARATOR)
    if len(fields) not in [2, 3]:
        return None

    src = fields[0]
    tgt = fields[1]
    alt = fields[2] if len(fields) == 3 else ''
    return src, tgt, alt
