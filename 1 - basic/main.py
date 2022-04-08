#!/usr/bin/env python3
"""
@Filename:    main.py
@Author:      dulanj
@Time:        08/04/2022 00:23
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
