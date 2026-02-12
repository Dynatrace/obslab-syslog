import requests
import time
from pathlib import Path
import os

def send_heartbeat():
    scenario = os.getenv("RepositoryName")
    container_id = Path("/etc/hostname").read_text().strip()

    body = {
        "scenario": scenario,
        "heartbeat_type": "devcontainer",
        "container_id": container_id,
        "timestamp": int(time.time())
    }

    resp = requests.post("https://webhook.site/dad48d2a-a3f4-464b-b60f-a49e760e3f03", json=body)
    resp2 = requests.post("https://zqsz7vy3cd.execute-api.us-east-1.amazonaws.com/default/ag-demo-heartbeats", json=body)

if __name__ == "__main__":
    send_heartbeat()