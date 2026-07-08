#!/usr/bin/env python3
"""WebSocket server that broadcasts messages to all connected clients."""

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed


# Stocke toutes les connexions clients actuellement actives.
active_connections = set()


async def connection_handler(websocket, path=None):
    """Handle one client connection and broadcast received messages."""
    # Ajoute le nouveau client dans la collection des connexions actives.
    active_connections.add(websocket)

    try:
        # Écoute les messages tant que le client reste connecté.
        async for message in websocket:
            # Prépare le message à envoyer à tous les clients.
            response = f"B:{message}"

            # Envoie le message à tous les clients actuellement connectés.
            await asyncio.gather(
                *[
                    connection.send(response)
                    for connection in active_connections.copy()
                ]
            )

    except ConnectionClosed:
        # Le client s'est déconnecté proprement ou brutalement.
        pass

    finally:
        # Retire le client de la collection des connexions actives.
        active_connections.discard(websocket)


async def main():
    """Start the WebSocket broadcast server."""
    # Démarre le serveur WebSocket sur localhost, port 8765.
    async with websockets.serve(connection_handler, "localhost", 8765):
        # Garde le serveur actif indéfiniment.
        await asyncio.Future()


if __name__ == "__main__":
    # Lance la fonction principale asynchrone.
    asyncio.run(main())
