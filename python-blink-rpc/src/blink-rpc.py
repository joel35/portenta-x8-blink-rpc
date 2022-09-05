import os
import time
from typing import Any

from msgpackrpc import Address as RpcAddress, Client as RpcClient, error as RpcError
import sys

# how long to wait in seconds between loop cycles
LOOP_INTERVAL = int(os.getenv("LOOP_INTERVAL", 1))

# The M4 Proxy address needs to be mapped via Docker's extra hosts
M4_PROXY_ADDRESS = sys.argv[1] or 'm4-proxy'
M4_PROXY_PORT = int(sys.argv[2]) or 5001
RPC_ADDRESS = RpcAddress(M4_PROXY_ADDRESS, M4_PROXY_PORT)

# list of RPC calls to make
RPC_CALLS = ['count', 'led']


def main() -> None:
    print_banner()

    try:
        rpc_loop(RPC_CALLS, RPC_ADDRESS, LOOP_INTERVAL)

    except KeyboardInterrupt:
        print('Stopped.')
        exit(0)


def print_banner() -> None:
    print()
    print("============================================")
    print("==       Portenta X8 M4 output            ==")
    print("============================================")
    print()


def rpc_loop(calls: list, rpc_address: RpcAddress, interval: int = 1) -> None:
    """Print data retrieved from m4 in a constant loop"""
    if not calls:
        print("No RPC calls defined")

    while True:
        for call in calls:
            if (value := get_data_from_m4(rpc_address, call)) is not None:
                print(f"{call}: ", value)
            else:
                print(f"{call}: no data!")

        time.sleep(interval)


def get_data_from_m4(address: RpcAddress, key: str) -> Any | None:
    """Send `key` value to RPC client and return received response"""
    try:
        client = RpcClient(address)
        return client.call(key)

    except RpcError.TimeoutError:
        print(f"Unable to retrieve {key} from the M4.")


if __name__ == '__main__':
    main()
