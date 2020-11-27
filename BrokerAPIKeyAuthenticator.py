import hashlib
import hmac
import json
# Generates an API signature.
# A signature is HMAC_SHA256(secret, data), hex encoded.


# secret = string
# data = json 
def generate_signature(secret, data):
    """Generate a request signature compatible with Broker CEX.IO."""
    # Remove whitespaces, tabs and new lines.
    message = bytes(''.join(json.dumps(data).split()), 'utf-8')
    # print("Computing HMAC: %s" % message)

    signature = hmac.new(bytes(secret, 'utf-8'), message, digestmod=hashlib.sha256).hexdigest()
    return signature
