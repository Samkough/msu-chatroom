# MSU ChatRoom
Creating a chatroom that can handle multiple clients for my final group project in CSIT340 - Computer Networks, taken at Montclair State University.

## Requirements
* Python 3.5+ (haven't tried w/ anything lower than 3.5)
* Java

## Outline
### Behaviors on ChatRoomServer
ChatRoomServer maintains the chat room. It will always maintain a set/list of active clients in the chat room. It will also manage all related messages (from and to the clients). The ChatRoomServer doesn’t need multiple threads to meet the requirements.
* Whenever a new client **joins** the chat room: the ChatRoomServer sends a welcome message to the newly joined client. It also notifies (broadcasts to) all existing clients in the chat room that a new client joined. It will add this new client to the active clients set/list.
* Whenever an existing client **leaves** the chat room: the ChatRoomServer notifies (broadcasts to) all existing clients that a client left the chat room. It removes the leaving client from the active clients set/list. (It also needs to cooperate with the leaving client program, so that the leaving client program can gracefully terminate.)
* Whenever an existing client **sends a message** to the chat room: the ChatRoomServer broadcasts the message to all other existing clients in the chat room. 
* The notifications and messages involved above should bear unique identifier of the client, for example, the IP address and the port number used by the client.


### Behaviors on ChatRoomClient
ChatRoomClient is the client program, allowing users to use the chat room service.
* The client automatically **joins** the chat room when the client program is run. This can be implemented by sending a special message to the ChatRoomServer, for example, “@_@Join”, “$$$JOIN”, or “!Join”, etc.
* The client allows the user to input a special message to **leave** the chat room, for example, “@_@Quit”, “$$$QUIT”, or “!Quit”, etc. When the user issues this message, make sure that the client program terminates gracefully, so as not to cause problems for the server, and not to affect the future rerunning of the client and running of new clients.
* When the user types in some message, the client **sends** the message to the ChatRoomServer. The message needs to be broadcast to all other clients (excluding the sending client) in the chat room. This is done by the server program.
* When the local client is running and in the chat room, it should always **wait for messages** sent from the chat room server. For example, when another client in the chat room sends a message to the chat room, the ChatRoomServer will send the message to this local client, because the server does broadcasting. 
* Notice that each client should do two things at the same time: **1.** Waiting for user’s input & sending the message out, and **2.** Waiting to receive message and print the message on the standard output. Thus, you are required to implement **multi-threading on the client** to allow it to do these two things simultaneously.

## Resources
Java multithreading:
* https://www.tutorialspoint.com/java/java_multithreading.htm
* https://www.geeksforgeeks.org/multithreading-in-java/

Python 2 multithreading:
* http://www.techbeamers.com/python-multithreading-concepts/
* https://www.tutorialspoint.com/python/python_multithreading.htm

Python 3 multithreading:
* https://www.tutorialspoint.com/python3/python_multithreading.htm