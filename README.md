# Tic-Tac-Toe ML Infra Engineer Code Screen Starter Code

This repo contains one solution to complete Adobe Research's
[ML Infrastructure Engineer code
screen](https://tic-tac-toe.ethos61-stage-va7.ethos.adobe.net/doc/infra/instructions.html).

The architecture involves three primary components:

 - The game service that's responsible for handling user requests. The  service is stateless such that there can be multiple instances of it.
 - A Redis container where the board positions of each game are persisted.
 - A Nginx web server which listens on port 5000 and distributes requests to all game service instances. It serves as a load balancer for the game service.

## How to run the code
To start the service with three containers of game service:

> docker-compose up --build --scale game=3

To stop it, just press '**CTRL + c**'.   To clear previous games, `docker-compose down` can be executed

The each API can be accessed from http://localhost:5000.  Each API will return an extra "host" field representing the container ID of the game service which handled the request. Example:

> curl -X POST http://localhost:5000/game
> 
    {
       "host": "0d522443eca9",
      "id": "NgwW5N",
      "status": "active",
      "turnCount": 0
    }
