from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware # CORS
from pydantic import BaseModel

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

@app.get('/sentence')
async def get_sentence():
    return {
         "sentence": "準備",
        "hiragana": "じゅんび",
        "romaji_map": [
            ["ju", "jyu", "jilyu", "zyu", "zilyu"],
            ["n", "nn"],
            ["bi"]
        ]
    }

sentence_storage = []

class SentenceRequest(BaseModel):
    sentence: str
    hiragana: str
    romaji_map: list[list[str]]

# 文章を追加
@app.post("/sentence")
async def create_sentence(data:SentenceRequest):
    sentence_id = len(sentence_storage)
    sentence_storage.append({"id": sentence_id, **data.model_dump()})
    return  {"message": "Sentence stored successfully", "id": sentence_id}

# 文章をすべて取得
@app.get("/sentence/all")
async def get_all_sentences():
    return {"sentence": sentence_storage}

# 指定されたidの文章を取得
@app.get("/sentence/{sentence_id}")
async def get_sentence(sentence_id: int):
    for sentence in sentence_storage:
        if sentence["id"] == sentence_id:
            return sentence
    raise HTTPException(status_code=404,detail="Sentence not found")

# 指定されたidの文章を削除
@app.delete("/sentence/{sentence_id}")
async def delete_sentence(sentence_id: int):
    for index,sentence in enumerate(sentence_storage):
        if sentence["id"] == sentence_id:
            del sentence_storage[index] #リストから削除
            return {"message": "Sentence deleted successfully", "id": sentence_id}
        
    raise HTTPException(status_code=404, detail="Sentence not found")