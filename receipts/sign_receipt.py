import json
import hashlib

def canonical_json(data):
    return json.dumps(
        data,
        sort_keys=True,
        separators=(",", ":")
    )

def sign_receipt(receipt, issuer="VERIDIAN_LOCAL"):
    payload = canonical_json(receipt)

    signature = hashlib.sha256(
        (payload + issuer).encode()
    ).hexdigest()

    signed_receipt = dict(receipt)

    signed_receipt["issuer"] = issuer
    signed_receipt["signature_algorithm"] = "SHA256_LOCAL"
    signed_receipt["signature"] = signature

    return signed_receipt

if __name__ == "__main__":
    receipt = {
        "decision": "ALLOW",
        "record_hash": "example_hash"
    }

    signed = sign_receipt(receipt)

    print(json.dumps(signed, indent=2))
