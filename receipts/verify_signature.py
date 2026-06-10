import json
import hashlib

def canonical_json(data):
    return json.dumps(
        data,
        sort_keys=True,
        separators=(",", ":")
    )

def verify_receipt(receipt):

    signature = receipt.get("signature")

    payload = dict(receipt)

    payload.pop("signature", None)

    issuer = payload.get("issuer")

    expected = hashlib.sha256(
        (canonical_json(payload) + issuer).encode()
    ).hexdigest()

    if signature == expected:
        print("SIGNATURE_VALID")
    else:
        print("SIGNATURE_INVALID")

if __name__ == "__main__":

    receipt = {
        "decision": "ALLOW",
        "record_hash": "example_hash",
        "issuer": "VERIDIAN_LOCAL",
        "signature_algorithm": "SHA256_LOCAL"
    }

    receipt["signature"] = hashlib.sha256(
        (canonical_json(receipt) + "VERIDIAN_LOCAL").encode()
    ).hexdigest()

    verify_receipt(receipt)
