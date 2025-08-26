## Start Demo

--8<-- "snippets/bizevent-start-demo.js"

=== "Run in Cloud"
    --8<-- "snippets/codespace-details-warning-box.md"
    --8<-- "snippets/start-demo-run-in-cloud.md"

=== "Run Locally"
    --8<-- "snippets/start-demo-run-locally.md"

## Understand Demo Environment

The Dynatrace OpenTelemetry Collector (`./dynatrace-otel-collector`) is automatically downloaded at startup. The collector is the syslog server. This collector distribution is officially supported by Dynatrace.

Data will be sent **to** the collector (from a device) and the collector will forward that data to Dynatrace.

The collector requires a configuration file. This is also already present (`config.yaml`).

To generate syslog data, we need a "fake" device to generate the data and send it to the syslog server (ie. the collector). For this, we use a Python script (`syslog_generator.py`).

The Python script:

* Reads `sample_log_lines.log`
* Uses these logs lines as a seed to generate random syslog entries
    * The `host`, `tag`, `level` and `pid` are randomised for each log line
* Sends the syslog entry via UDP to the collector

### Understand Collector Configuration

Understanding the configuration of the collector is key to understanding how the data gets from your devices into Dynatrace.

Note: You do not need to modify `config.yaml` file.

#### Receivers

```
receivers:
  syslog:
    udp:
      listen_address: "127.0.0.1:54526"
    protocol: rfc3164
```

The receivers block describes how data is received by the collector.

In this case, the [syslog receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/syslogreceiver){target=_blank} is listening for incoming `UDP` connections on port `54526` and expecting incoming messages to by formatted in [RFC3164 format](https://datatracker.ietf.org/doc/html/rfc3164){target=_blank}.

#### Exporters

```
exporters:
  debug:
    verbosity: detailed
  otlphttp:
    endpoint: "https://YourTenantID.live.dynatrace.com/api/v2/otlp"
    headers:
      Authorization: "Api-Token ${env:DT_API_TOKEN}"
```

The exporters block defines what happens to the data at the point it leaves the collector.

The `otlphttp` exporter sends data to an endpoint in OpenTelemetry Protocol (OTLP) format via HTTPS. Dynatrace natively understands the OTLP format.

Notice that an environment variables is referenced: `DT_API_TOKEN` you may recall these from the form you completed when the codespace started. The Dynatrace URL is automatically build (by the codespace at startup) and placed into the config.yaml file. You do not need to change `config.yaml`.

These environment variables are already set for you, so you don't need to do anything else.

#### Pipelines

```
service:
  pipelines:
    logs:
      receivers: [syslog]
      exporters: [otlphttp]
```

The pipelines block defines how the collector components are connected in an end-to-end pipeline.

In this case, `1` pipeline (dealing with log data) is defined. This pipeline will receive data using the `syslog` receiver and export it to the `otlphttp` exporters simultaneously.

<div class="grid cards" markdown>
- [Click here to continue :octicons-arrow-right-24:](run-demo.md)
</div>
