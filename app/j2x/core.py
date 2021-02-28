from enum import Enum
from typing import Awaitable

from dicttoxml import dicttoxml
from jsonpath_ng import parse

from app.j2x import fetcher
from app.j2x.response import FailureResponse, SuccessResponse


class ReturnFormat(Enum):
    JSON = 1
    XML = 2


async def get(res, url, path, fmt):
    jsp = parse(path)

    j = await fetcher.get(url)
    output = [v.value for v in jsp.find(j)]

    if fmt is ReturnFormat.XML:
        return dicttoxml(output)

    else:
        return SuccessResponse(result=output)
