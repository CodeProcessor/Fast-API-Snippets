#!/usr/bin/env python3
"""
@Filename:    main.py
@Author:      dulanj
@Time:        08/04/2022 00:23
"""
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items")
def read_item(
        cai_request_id: str,
        source_doc_source_mime_type: Optional[str] = "pdf",
        source_doc_target_mime_type: Optional[str] = "html",
):
    return {"CAI req ID": cai_request_id, "source mime": source_doc_source_mime_type, "target mime": source_doc_target_mime_type}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
