import asyncio
import socket
from core.Player import *
from mobs.spown import StartSpowning
from ServerCallDic import callList
from GlobalData import connected_clients
from Util import *
async def handle_client(reader, writer):
    client_address = writer.get_extra_info('peername')
    print("Client connected:", client_address)

    client_socket = writer.get_extra_info('socket')
    p = Player(client_socket, client_address)
    connected_clients[client_socket] = p

    try:
        while True:
            # Receive data from the client
            data = await reader.read(1024)
            if not data:
                # remove player in area for other clients
                callList['CallDisconnected'].data("",connected_clients[client_socket])
                # No more data, connection closed by client
                print("Connection closed by client:", client_address)
                break

            received_data = data.decode()
            data = received_data.split("#")
            callIndex = data[0]

            # Execute the intended operation
            callList[callIndex].data(data[1], connected_clients[client_socket])

    finally:
        # Clean up the connection
        writer.close()
        await writer.wait_closed()


        # Remove the client from the dictionary when the connection is closed
        if client_socket in connected_clients:
            connected_clients[client_socket].OnDelete()
            del connected_clients[client_socket]

        

async def start_server():
    server_address = (SERVER_IP, SERVER_PORT)

    server = await asyncio.start_server(
        handle_client, *server_address, reuse_address=True)

    print("Server started. Waiting for a client to connect...")
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    #Adding functions to activate every 10 seconds
    triggerEvery10Sec.append(StartSpowning)
    triggerEvery10Seconds()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server())
    