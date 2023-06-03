from fastapi import FastAPI
import logging
from hello import sum_xy
from data_models import SamplePostRequest


log_format = "[%(name)s][%(levelname)-6s] %(message)s"
logging.basicConfig(format=log_format)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

app = FastAPI()

@app.get("/home")
def home():
    return "hello"


@app.get("/sum/{c}")
def sum_xy_endpoint(c: str, a: int, b: int):
    logger.info("Recievevd request.")

    try:
        sum_xy("1", 7)
    except:
        logger.error("NOOOOOOOOOOOOOOOOOOOOOOOOOO")

    output = c + " " + str(sum_xy(a, b))

    return output


@app.post("/predict")
def predict(request: SamplePostRequest):

    return [request.a + request.b]