from fastapi import APIRouter
from modules.module_template import template
from interfaces.interface_template import TemplateResponse

router = APIRouter()


@router.get("/", response_model=TemplateResponse)
def template_api(text: str = 'example text'):
    return template(text)
