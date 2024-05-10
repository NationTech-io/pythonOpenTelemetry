# https://opentelemetry.io/docs/languages/python/getting-started/

from random import randint
from fastapi import FastAPI, Request
import uvicorn
import logging

from opentelemetry import trace
from opentelemetry import metrics

from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter

from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader


app = FastAPI()

otlp_http_exporter = OTLPMetricExporter()
metric_reader = PeriodicExportingMetricReader(exporter=otlp_http_exporter)
provider = MeterProvider(metric_readers=[metric_reader])

# Sets the global default meter provider
metrics.set_meter_provider(provider)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

tracer = trace.get_tracer("diceroller.tracer")
meter = metrics.get_meter("diceroller.meter")

roll_counter = meter.create_counter(
    "dice.rolls",
    description="The number of rolls by roll value",
    unit="1"
)

@app.get("/")
def read_root():
    #with tracer.start_as_current_span("handle_request"):
    #    return {"Hello": "World"}
    logger.debug("debuggggggg")
    return {"Hello": "World"}

@app.get("/hello")
def read_hello():
    logger.debug("Yooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")


@app.get("/rolldice")
def roll_dice(request: Request):
    # This creates a new span that's the child of the current one
    with tracer.start_as_current_span("roll") as roll_span:
        player = request.query_params.get('player', default=None)
        result = str(roll())
        roll_span.set_attribute("roll.value", result)
        # This adds 1 to the counter for the given roll value
        roll_counter.add(1, {"roll.value": result})
        if player:
            logger.warn("{} is rolling the dice: {}", player, result)
        else:
            logger.warn("Anonymous player is rolling the dice: %s", result)
        return result

def roll():
    return randint(1, 6)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8800)

