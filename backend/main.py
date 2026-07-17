from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

origins = ["http://localhost:5174"]

# セキュリティ面のコード。Reactアプリと通信の際の権限関係。
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def Hello():
    return {"Hello": "World!"}
