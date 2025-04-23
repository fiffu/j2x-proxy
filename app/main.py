import aiohttp
from fastapi import FastAPI, Response
from fastapi.responses import PlainTextResponse, RedirectResponse

from j2x import core
from j2x.response import BaseResponse, FailureResponse, SuccessResponse


JsonPath = str

app = FastAPI()


@app.get('/ping', response_model=BaseResponse)
async def ping():
    return SuccessResponse(result='ok')


@app.get('/json', response_model=BaseResponse)
async def json(res: Response, url: str, path: str):
    """Get a JSON response from the given url and extract a using the given JSONPath."""
    return await _work(res, url, path, core.ReturnFormat.JSON)


@app.get('/xml', response_class=PlainTextResponse)
async def xml(res: Response, url: str, path: str = '$') -> PlainTextResponse:
    """Get a JSON response from the given url and extract a using the given JSONPath."""
    return await _work(res, url, path, core.ReturnFormat.XML)


async def _work(res: Response, url: str, path: str, fmt: core.ReturnFormat):
    try:
        return await core.get(res, url, path, fmt)

    except aiohttp.ClientResponseError as err:
        res.status_code = err.status

        content = None
        if err.history:
            content = str(err.history[-1].content)

        msg = (f'GET {err.request_info.real_url} returned: {err.status} {err.message}')

        return FailureResponse(message=msg, result=content)

    except BaseException as err:
        msg = f'{err.__class__.__name__}: {str(err)}'
        res.status_code = 500
        return FailureResponse(message=msg)


@app.get('/')
async def root():
    return RedirectResponse(url='/docs')
