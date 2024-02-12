from fastapi import FastAPI
import route

app = FastAPI()

app.include_router(route.app)


    

