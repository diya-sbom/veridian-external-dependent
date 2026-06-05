import requests
import sys
import json

API_URL = "http://127.0.0.1:8000/verify"

payload = {
    "state": {
        "valid": True
    },
    "action": {
        "allowed": True
    }
}
try:
    response = requests.post(API_URL, json=payload, timeout=5)
except Exception as e:
    print("HALT: Veridian API unavailable")
    sys.exit(1)

receipt = response.json()

with open("verification_receipt.json", "w") as f:
    json.dump(receipt, f, indent=2)

if response.status_code != 200:
    print("HALT: verification failed")
    sys.exit(1)

if receipt.get("decision") not in ["PASS", "ALLOW"]:
    print("HALT: decision denied")
    sys.exit(1)

print("EXECUTION_ALLOWED")
