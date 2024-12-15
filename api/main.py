from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# import sys
# print(sys.path)
from .routers import chat, gpt, category, sort, session, restart, value


app = FastAPI()

origins = [
    "http://localhost:5173",  # React development server
    # add more origins if needed, like your production frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows requests from these origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# app.include_router(chat.router, prefix="/api", tags=["Chat"])
app.include_router(chat.router, tags=["Chat"])
app.include_router(gpt.router, tags=["GPT"])
app.include_router(category.router, tags=["CATEGORY"])
app.include_router(sort.router, tags=["SORT"])
app.include_router(session.router, tags=["SESSION"])
app.include_router(restart.router, tags=["RESTART"])
app.include_router(value.router, tags=["VALUE"])

