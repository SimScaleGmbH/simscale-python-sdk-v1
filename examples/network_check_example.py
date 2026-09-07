#!/usr/bin/env python
"""Network check example using the SimScale SDK v1.

Measures API roundtrip and storage upload throughput from this environment.
The transfer size is capped here to keep the example fast; for real
diagnostics run without max_tier_bytes (or use the simscale-network-check
command), so fast links are measured with larger transfers.
"""

import json

from simscale_sdk_v1 import SimScaleSDK

sdk = SimScaleSDK()

result = sdk.network_check(max_tier_bytes=4 * 1024 * 1024)

print(json.dumps(result.to_dict(), indent=2))

if result.errors:
    raise RuntimeError(f"Network check reported errors: {result.errors}")
if not result.upload_single_mbits or result.upload_single_mbits <= 0:
    raise RuntimeError("Expected a positive single-stream upload rate")

print("\nDone!")
