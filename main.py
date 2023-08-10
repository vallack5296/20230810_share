# --- sample-app/main.py ---

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from mangum import Mangum

from src.env import get_env

# FastAPIとはPythonのWebアプリケーション用に作られたフレームワーク
app = FastAPI(
    redoc_url="/api/redoc",
    docs_url="/api/docs", # FastAPIが管理している一覧がでてくる
    openapi_url="/api/docs/openapi.json",
    root_path=get_env().api_gateway_base_path,
)
allow_origins = ["*"]


@app.get("/api/hello") #/api/hello入力されると画面に「{"hoge":"/prd"}」と出力される。
def hello():
    env = get_env()
    return {"hoge": env.api_gateway_base_path} # env.api_gateway_base_pathは環境変数から取得してきている。詳しくはserverless.ymlファイルのAPI_GATEWAY_BASE_PATH。

@app.get("/api/test") #/api/hello入力されると画面に「{"hoge":"/prd"}」と出力される。
def test0724():
    env = get_env()
    return {"0724": env.api_gateway_base_path}

app.mount("/", StaticFiles(directory=f"./static", html=True), name="static") #/以降にきたものはstatic以下のものを参照する。

handler = Mangum(app)