# j2x-proxy

```py
json2xml = lambda url, jsonpath: '<xml>'
```

j2x-proxy is a [FastAPI](https://fastapi.tiangolo.com/) server with some GET endpoints
that:

1. Read JSON from an API,
2. Extract specific elements using JSONPath, then
3. Return the elements in an XML document.

Alternatively, the elements can be returned in a JSON response for your nefarious needs.

## Example

Let's say you want to get some data off Yahoo Finance:

```sh
# url:  https://query1.finance.yahoo.com/v7/finance/spark?symbols=BTC-USD
# path: $..regularMarketPrice
curl -X GET "http://localhost:8000/xml?url=https%3A%2F%2Fquery1.finance.yahoo.com%2Fv7%2Ffinance%2Fspark%3Fsymbols%3DBTC-USD&path=%24..regularMarketPrice"
# <?xml version="1.0" encoding="UTF-8" ?><root><item type="float">46944.78</item></root>
```

## Setup

```sh
workon j2x-proxy  # or your choice of porcelain...
pip install -r requirements.txt
uvicorn j2x.main:app --reload
```

The auto-generated handily doubles as a GUI - `http://localhost:8000/docs`

## References

**JSONPath** - [try it online](https://jsonpath.com/) / [reference](https://goessner.net/articles/JsonPath/index.html#e2)
