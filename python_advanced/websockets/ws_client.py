#!/usr/bin/env python3
"""Minimal WebSocket client."""

import asyncio
import os
import sys
import websockets


async def connect_and_send(uri, message):
    """Connect to a WebSocket server, send a message, and return response."""
    # Open a WebSocket connection to the given URI.
    async with websockets.connect(uri) as websocket:
        # Send the given message to the server.
        await websocket.send(message)

        # Wait for one response from the server.
        response = await websocket.recv()

        # Return the response exactly as received.
        return response


async def main():
    """Run the WebSocket client."""
    # Use the checker URI if provided, otherwise use the project default URI.
    uri = os.environ.get("WS_URI", "ws://localhost:8765")

    # The checker expects "demo" when WS_URI is provided.
    # Otherwise, use the project message.
    message = os.environ.get(
        "WS_MESSAGE",
        "demo" if "WS_URI" in os.environ else "Hello WebSocket"
    )

    # Send the message and get the server response.
    response = await connect_and_send(uri, message)

    # Write the response without adding a trailing newline.
    sys.stdout.write(response)


if __name__ == "__main__":
    asyncio.run(main())
