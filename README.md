the file to look at is `server.py`

Followed this: https://opentelemetry.io/docs/languages/python/getting-started/

traces and logs worked well, but not metrics (not sent)

For metrics, I based myself on this: https://opentelemetry.io/docs/languages/python/instrumentation/#metrics

and made a few modifs, using the `otlp_http_exporter`

Env vars:
```
OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
OTEL_EXPORTER_OTLP_HEADERS=authorization=<hyperdx key>
OTEL_EXPORTER_OTLP_ENDPOINT=http://192.168.12.160:4318
OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=false
OTEL_SERVICE_NAME=PYTHON

HYPERDX_ENABLE_ADVANCED_NETWORK_CAPTURE=1
HYPERDX_API_KEY=<hyperdx key>

DEBUG=true
```

Starting the app:
```
$ opentelemetry-instrument python server.py
```
or
```
$ opentelemetry-instrument --traces_exporter console --metrics_exporter console --logs_exporter console python server.py
```


