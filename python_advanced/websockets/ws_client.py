#!/usr/bin/env python3
"""Minimal WebSocket client."""

import asyncio
import websockets


async def connect_and_send():
    """Connect to the server, send a message, and print the response."""
    # Define the WebSocket server URI.
    uri = "ws://localhost:8765"

    # Message required by the project.
    message = "Hello WebSocket"

    # Open a WebSocket connection to the server.
    async with websockets.connect(uri) as websocket:
        # Send the exact message to the server.
        await websocket.send(message)

        # Wait for the server response.
        response = await websocket.recv()

        # Print the response exactly as received.
        print(response)


if __name__ == "__main__":
    asyncio.run(connect_and_send())