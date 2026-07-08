#!/usr/bin/env python3
"""Minimal WebSocket client."""

import asyncio
import websockets


async def send_message():
    """Connect to the WebSocket server, send a message, and print response."""
    # Define the WebSocket server URI.
    uri = "ws://localhost:8765"

    # Define the exact message required by the project.
    message = "Hello WebSocket"

    # Open a WebSocket connection to the server.
    async with websockets.connect(uri) as websocket:
        # Send the message to the server.
        await websocket.send(message)

        # Wait for one response from the server.
        response = await websocket.recv()

        # Print the response exactly as received.
        print(response)


if __name__ == "__main__":
    asyncio.run(send_message())
