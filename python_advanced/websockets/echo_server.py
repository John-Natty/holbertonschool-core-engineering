#!/usr/bin/env python3
"""Minimal WebSocket echo server."""

import asyncio
import websockets


async def connection_handler(websocket, path=None):
    """Handle a client connection and echo received messages."""
    # Listen continuously for messages from the connected client.
    async for message in websocket:
        # Send back the exact same message without modification.
        await websocket.send(message)


async def main():
    """Start the WebSocket server on localhost port 8765."""
    # Create the WebSocket server using the required handler function.
    async with websockets.serve(connection_handler, "localhost", 8765):
        # Keep the server running forever.
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
