import json
from typing import Dict, Optional

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

DEFAULT_CONTENT = {
    "web_title": "Như {...} Long",
    "text1": "Hế luu bé {...}!",
    "text2": "{...} có điều này muốn hỏi {...} nhớ phải trả lời thật lòng nhaaa.",
    "text3": "{...} yêu {...} có phải không nào ._.",
    "text4": "Nếu {...} ko trả lời mà thoát ra tức là muốn làm {...} rùi đó nha :v",
    "text5": "Khum iu {...} nha :))",
    "text6": "Iu {...} nhèo nhèo :))",
    "text7": "Sao {...} iu {...} dị. :vvvv",
    "text8": "Gửi cho {...} di <3",
    "text9": "Vì {...} ..........",
    "text10": "Vũ trụ này là do {...} tạo ra cho riêng 2 đứa mình",
    "text11": "Mời em vào vũ trụ của riêng chúng ta :DDDDDDDDDDDDD",
    "text12": "Ok lunn <3"
}


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    with open("static/js/config.json", encoding="utf-8") as f:
        data: dict = json.load(f)
        return templates.TemplateResponse(
            request=request, name="index.html",
            context={"web_title": data.get("web_title", DEFAULT_CONTENT["web_title"])}
        )


@app.patch("/content", )
def patch_content(content: Dict[str, Optional[str]]):
    with open("static/js/config.json", encoding="utf-8") as f:
        data: dict = json.load(f)

        for key, value in content.items():
            data[key] = value
            if value is None and key not in DEFAULT_CONTENT:
                data.pop(key)
            if value is None and key in DEFAULT_CONTENT:
                data[key] = DEFAULT_CONTENT[key]

        json.dump(data, open("static/js/config.json", "w", encoding="utf-8"))
        return data


@app.get("/content")
def get_content():
    with open("static/js/config.json", encoding="utf-8") as f:
        return json.load(f)
