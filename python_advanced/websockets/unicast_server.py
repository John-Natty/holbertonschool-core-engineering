#!/usr/bin/env python3
"""WebSocket server that sends responses only to the sender."""

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed


# Stocke toutes les connexions clients actuellement actives.
active_connections = set()


async def connection_handler(websocket, path=None):
    """Handle one client connection and send responses only to that client."""
    # Ajoute le nouveau client dans la collection des connexions actives.
    active_connections.add(websocket)

    try:
        # Écoute les messages tant que le client reste connecté.
        async for message in websocket:
            # Envoie la réponse uniquement au client qui a envoyé le message.
            await websocket.send(f"U:{message}")

    except ConnectionClosed:
        # Le client s'est déconnecté proprement ou brutalement.
        pass

    finally:
        # Retire le client de la collection des connexions actives.
        active_connections.discard(websocket)


async def main():
    """Start the WebSocket unicast server."""
    # Démarre le serveur WebSocket sur localhost, port 8765.
    async with websockets.serve(connection_handler, "localhost", 8765):
        # Garde le serveur actif indéfiniment.
        await asyncio.Future()


if __name__ == "__main__":
    # Lance la fonction principale asynchrone.
    asyncio.run(main())
