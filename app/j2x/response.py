from typing import Optional, Union

from fastapi.responses import HTMLResponse
from pydantic import BaseModel


class BaseResponse(BaseModel):
    success: bool
    message: Optional[str]
    result: Optional[Union[dict, list, str, int, float]]

class SuccessResponse(BaseResponse):
    success = True

class FailureResponse(BaseModel):
    success = False
    message = 'Internal server error.'

class XMLResponse(HTMLResponse):
    pass
