This repo contains an example on using OpenTelemetry in a python app to send logs, traces, metrics to an hyperdx backend

Documentation used:
- https://www.hyperdx.io/docs/install/python
- https://opentelemetry.io/docs/languages/python/getting-started/

The [hyperdx distribution of OpenTelemetry for python](https://github.com/hyperdxio/hyperdx-py) made to simplify the setup is used in this project.

I based myself on [this example](https://opentelemetry.io/docs/languages/python/instrumentation/#metrics)

traces and logs worked well, but metrics were not sent.

I made a few modifs, defined a MeterProvider, OTLPMetricExporter and PeriodicExportingMetricReader myself, and made the metrics work this way.

I am currently sending all that to an on-premise installation of hyperdx running in http.

Env vars:
```
OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
OTEL_EXPORTER_OTLP_HEADERS=authorization=<hyperdx key>
OTEL_EXPORTER_OTLP_ENDPOINT=http://<HyperDX_IP>:<HyperDX_PORT>
OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=false
OTEL_SERVICE_NAME=RollTheDice

HYPERDX_ENABLE_ADVANCED_NETWORK_CAPTURE=1
HYPERDX_API_KEY=<hyperdx key>

DEBUG=true
```

How to run
```
pythonOpenTelemetry$ python -m venv venv
pythonOpenTelemetry$ source ./venv/bin/activate
(venv) pythonOpenTelemetry$ pip install -r requirements.txt
(venv) pythonOpenTelemetry$ vi env # --> setup your env variables properly
(venv) pythonOpenTelemetry$ source ./env
(venv) pythonOpenTelemetry$ opentelemetry-instrument python server.py
```
