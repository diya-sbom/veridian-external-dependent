import requests
import json

response = requests.post(
    "http://127.0.0.1:8000/verify",
    json={
        "state": {
            "receipt": "veridian_external_receipt.json"
        }
    }
)

with open("verification_receipt.json", "w") as f:
    json.dump(response.json(), f, indent=2)

if response.status_code == 200:
    print("EXECUTION_ALLOWED")
else:
    print("HALT")
