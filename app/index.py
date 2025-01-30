from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# JSON data with 100 students (Example)
students_data = [{"name":"CQFGT","marks":93},{"name":"IM49L4E","marks":92},{"name":"D5v","marks":23},{"name":"YsP4UOlL","marks":13},{"name":"Tgt","marks":18},{"name":"K","marks":47},{"name":"SSV1py","marks":19},{"name":"fcXqubp","marks":99},{"name":"3","marks":78},{"name":"u2c3Q4HdN","marks":11},{"name":"1qoBTaXLn","marks":22},{"name":"SpF","marks":60},{"name":"1KyYX3V","marks":13},{"name":"gN30zaxUo","marks":38},{"name":"mJLAEypK","marks":4},{"name":"kX39Uunl","marks":44},{"name":"uPbVELb24","marks":32},{"name":"e2A52nLR","marks":91},{"name":"1o6WjySJZ","marks":68},{"name":"gY0Ot1f","marks":83},{"name":"HvAns4zx","marks":99},{"name":"vEL6uH6ITf","marks":53},{"name":"whm18O7w","marks":62},{"name":"uw8AQ9CowM","marks":88},{"name":"to","marks":38},{"name":"ghm0","marks":14},{"name":"LymvgWCr","marks":22},{"name":"I3Yu6Wh","marks":10},{"name":"c5gCcp3VG","marks":58},{"name":"GTt","marks":59},{"name":"4fg7QdZBU","marks":35},{"name":"LZ","marks":39},{"name":"6l5s","marks":40},{"name":"mWJ6","marks":10},{"name":"Zf4fU4ocsx","marks":58},{"name":"mlsU1R","marks":65},{"name":"wqXso7lkJ","marks":91},{"name":"CmPoP5o7P","marks":88},{"name":"wa3WCb","marks":30},{"name":"ybCug3a4","marks":34},{"name":"oNFSb","marks":37},{"name":"6RG","marks":23},{"name":"cxr1nzso","marks":19},{"name":"KsP4xiS5pP","marks":96},{"name":"pET8KeYNEL","marks":0},{"name":"EK5q1oQEW","marks":15},{"name":"xLgXva","marks":71},{"name":"SdwgNEuA","marks":32},{"name":"R","marks":9},{"name":"x","marks":40},{"name":"UoZSDjOK","marks":37},{"name":"fnV","marks":16},{"name":"iCCyktlPI","marks":53},{"name":"2k","marks":70},{"name":"gDvvYk","marks":23},{"name":"YxZ","marks":53},{"name":"uNIg","marks":26},{"name":"PtCrGy2Ga","marks":94},{"name":"L","marks":9},{"name":"fxxm","marks":94},{"name":"jVfQiuWE","marks":38},{"name":"rT","marks":34},{"name":"tbo","marks":68},{"name":"t","marks":38},{"name":"gbiR","marks":97},{"name":"NuEF","marks":62},{"name":"C0Q4rOI","marks":75},{"name":"Dm2xD6u","marks":7},{"name":"J","marks":49},{"name":"MWnPcuGw","marks":58},{"name":"akpxIqhs","marks":88},{"name":"Uh","marks":1},{"name":"lE7","marks":40},{"name":"n","marks":44},{"name":"gfO1LFBTH2","marks":63},{"name":"MREkx","marks":4},{"name":"w7suk","marks":53},{"name":"ZM","marks":1},{"name":"NGFjKy","marks":46},{"name":"0mFhZZGx","marks":83},{"name":"8ccY","marks":43},{"name":"X1G","marks":28},{"name":"S","marks":38},{"name":"j","marks":19},{"name":"kjbw5C3Q9","marks":1},{"name":"e3","marks":43},{"name":"MPEh","marks":94},{"name":"YqHtHYwH","marks":27},{"name":"sjkLdh1N","marks":54},{"name":"8kTWFE8U4","marks":32},{"name":"wJQRUG3c","marks":81},{"name":"z4UFABg","marks":19},{"name":"u9","marks":35},{"name":"QIJytxCb1O","marks":67},{"name":"W","marks":16},{"name":"EGTG","marks":45},{"name":"gEQ","marks":60},{"name":"nnRL","marks":89},{"name":"Vlhpogw","marks":28},{"name":"r","marks":5}]
@app.get("/api")
async def get_marks(name: list[str] = Query(None)):
    """
    Fetch marks of students by name.
    Example usage:
    - `/api?name=ho8ePmxFs` -> {"marks": [70]}
    - `/api?name=ho8ePmxFs&name=Zfmi` -> {"marks": [70, 55]}
    """
    if name:
        marks = [next((s["marks"] for s in students_data if s["name"] == n), None) for n in name]
        return {"marks": marks}
    return {"marks": []}
