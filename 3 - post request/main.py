"""
Copyright (C) CUBE Content Governance Global Limited - All Rights Reserved
Unauthorized copying of this file, via any medium is strictly prohibited
Proprietary and confidential
Written by Dulan Jayasuriya <dulan.jayasuriya@cube.global>, 08 April 2022
"""
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    cai_request_id: str
    source_doc_source_mime_type: Optional[str] = "pdf"
    source_doc_target_mime_type: Optional[str] = "html"


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items/")
async def create_item(item: Item):
    return item

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
