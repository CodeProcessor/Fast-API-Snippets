"""
Copyright (C) CUBE Content Governance Global Limited - All Rights Reserved
Unauthorized copying of this file, via any medium is strictly prohibited
Proprietary and confidential
Written by Dulan Jayasuriya <dulan.jayasuriya@cube.global>, 08 April 2022
"""
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

tags_metadata = [
        {
            "name": "POST",
            "description": "This API endpoint is a mock endpoint for post requests."
        },
        {
            "name": "Get",
            "description": "This API endpoint is a mock endpoint for get requests."
        }
]


class Item(BaseModel):
    cai_request_id: str
    source_doc_source_mime_type: Optional[str] = "pdf"
    source_doc_target_mime_type: Optional[str] = "html"


fast_app = FastAPI(
    title="FAST API",
    description="This is a test FastAPI application",
    version="1.0.0",
    terms_of_service="https://policies.google.com/terms?hl=en-US",
    openapi_tags=tags_metadata
)


@fast_app.get("/")
def read_root():
    return {"Hello": "World"}


@fast_app.post("/post_items", tags=["POST"])
async def create_item(item: Item):
    return item


@fast_app.get("/get_items", tags=["Get"])
def read_item(
        cai_request_id: str,
        source_doc_source_mime_type: Optional[str] = "pdf",
        source_doc_target_mime_type: Optional[str] = "html",
):
    return {"CAI req ID": cai_request_id, "source mime": source_doc_source_mime_type,
            "target mime": source_doc_target_mime_type}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(fast_app, host="0.0.0.0", port=8000)
