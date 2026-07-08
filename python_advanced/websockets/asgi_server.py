#!/usr/bin/env python3
"""ASGI application with HTTP and WebSocket routes."""

from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocketDisconnect


async def homepage(request):
    """Serve a simple HTML homepage."""
    # Page HTML affichée quand on visite http://localhost:8000.
    html_content = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>WebSocket App</title>
        </head>
        <body>
            <h1>WebSocket App</h1>
            <input id="messageInput" type="text" />
            <button onclick="sendMessage()">Send</button>
            <ul id="messages"></ul>

            <script>
                const ws = new WebSocket("ws://localhost:8000/ws");
                const messagesList = document.getElementById("messages");

                ws.onmessage = function(event) {
                    const li = document.createElement("li");
                    li.textContent = event.data;
                    messagesList.appendChild(li);
                };

                function sendMessage() {
                    const input = document.getElementById("messageInput");
                    ws.send(input.value);
                    input.value = "";
                }
            </script>
        </body>
    </html>
    """
    return HTMLResponse(html_content)


async def websocket_endpoint(websocket):
    """Accept WebSocket connections and echo received messages."""
    # Accepte la connexion WebSocket avant tout échange.
    await websocket.accept()

    try:
        while True:
            # Reçoit un message texte depuis le client.
            message = await websocket.receive_text()

            # Renvoie exactement le même message au même client.
            await websocket.send_text(message)

    except WebSocketDisconnect:
        # Le client s'est déconnecté, on ne fait rien de plus.
        pass


# Application ASGI utilisée par Uvicorn avec asgi_server:app.
app = Starlette(
    routes=[
        Route("/", homepage),
        WebSocketRoute("/ws", websocket_endpoint),
    ]
)
