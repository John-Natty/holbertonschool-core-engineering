#!/usr/bin/env python3
"""Minimal WebSocket echo server."""

import asyncio
import websockets


async def echo(websocket, _path=None):
    """Receive messages from a client and send them back unchanged."""
    # The async loop keeps listening while the client stays connected.
    async for message in websocket:
        # Send back the exact same message to the same client.
        await websocket.send(message)


async def main():
    """Start the WebSocket server and keep it running forever."""
    # Start a WebSocket server on localhost, port 8765.
    async with websockets.serve(echo, "localhost", 8765):
        # Keep the server alive indefinitely.
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
