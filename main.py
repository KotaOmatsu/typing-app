from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # CORS

app = FastAPI()

# CORSの設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js からのリクエストを許可
    allow_credentials=True,
    allow_methods=["*"],  # 全てのHTTPメソッドを許可
    allow_headers=["*"],  # 全てのヘッダーを許可
)

@app.get("/")
async def home():
    return {"message": "Hello, FastAPI!"}

