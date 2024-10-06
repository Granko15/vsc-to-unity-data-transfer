import asyncio
import websockets

async def handle_client(websocket, path):
    async for message in websocket:
        print(f"Message received: {message}")
        # Process the message and send a response if needed
        if message == "get_line_number":
            await websocket.send("You are on line 42")
        elif message.startswith("jump_to_line"):
            # Respond with a command for VS Code
            line_number = message.split(":")[1]
            await websocket.send(f"Jumping to line {line_number}")

async def start_server():
    server = await websockets.serve(handle_client, "localhost", 8765)
    print("Server started")
    await server.wait_closed()

# Start the server
asyncio.run(start_server())
