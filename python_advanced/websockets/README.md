# Real-time communication with WebSockets

## Introduction

Traditional HTTP communication follows a request–response model, where the client initiates every interaction and the server responds. This model is not suitable for applications that require continuous updates, such as chat systems, live dashboards, or collaborative tools.

WebSockets address this limitation by establishing a persistent connection. Once the connection is open, both the client and the server can send messages at any time without reopening the connection.

In this project, you will work with WebSockets, a communication protocol that enables real-time, bidirectional data exchange between a client and a server.

## Learning Objectives

By the end of this project, you should be able to:

- Implement a WebSocket server using asynchronous programming
- Handle multiple concurrent client connections
- Send and receive messages in real time
- Implement different message exchange patterns
- Enforce a defined message format when required

## General Requirements

Environment used for correction:

- Ubuntu 20.04
- Python 3.x