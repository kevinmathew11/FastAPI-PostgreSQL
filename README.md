# FastAPI-PostgreSQL
A starter kit for FAST using and Postgres database.

FastAPI is using Pydantic library for types and starlette framework under the hood
FastAPI also provide amazing support for swagger API docs

    from fastapi import FastAPI. : IMPORT 
    app = FastAPI()              : INSTANCE
    @app.get('/')                : DECORATE
    def index():                 : FUNCTION
      return 'Welcome to FASTAPI Application'
