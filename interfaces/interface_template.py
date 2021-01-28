from pydantic import BaseModel
from typing import Optional, Dict


class TemplateResponse(BaseModel):
    res: str
