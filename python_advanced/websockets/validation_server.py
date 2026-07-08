#!/usr/bin/env python3
"""WebSocket server that validates incoming messages."""

import asyncio
import websockets


async def connection_handler(websocket, path=None):
    """Handle a client connection and validate each received message."""
    # Listen continuously while the client stays connected.
    async for message in websocket:
        # Remove leading and trailing whitespace only for validation.
        cleaned_message = message.strip()

        # If the cleaned message is empty, reject it.
        if cleaned_message == "":
            await websocket.send("ERR:EMPTY")
        else:
            # Send the original valid message with the required OK prefix.
            await websocket.send(f"OK:{message}")


async def main():
    """Start the WebSocket validation server."""
    # Start the server on localhost, port 8765.
    async with websockets.serve(connection_handler, "localhost", 8765):
        # Keep the server running forever.
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
