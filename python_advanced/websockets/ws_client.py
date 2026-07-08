#!/usr/bin/env python3
"""Minimal WebSocket client."""

import asyncio
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
    """Run the client with the required default message."""
    # Required server URI for the project.
    uri = "ws://localhost:8765"

    # Required message for the project.
    message = "Hello WebSocket"

    # Send the message and get the response.
    response = await connect_and_send(uri, message)

    # Print only the response, exactly as received.
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
