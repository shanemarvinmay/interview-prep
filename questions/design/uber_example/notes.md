# Example Question: Design Uber (ride sharing app)
<a href="https://www.youtube.com/watch?v=R_agd5qZ26Y&list=WL&index=10" target="_blank">Source</a>

## Requirements
* rider selectes pickup point on map
* rider request ride
* rider can view pickup ETA 
* rider can view price
* Drivers and riders are matched
* Driver accepts rides
* Rider receives info about driver (location updates in real time)

# Notes
[Bookmark 3:00](https://youtu.be/R_agd5qZ26Y?t=180)
* BAD: just setting up services/db as is with first design will cause a lot of congestion as things get busy
    * Any one of the requirements being executed would need to hit many of the components before being completed.
    * Answer: "Event bus" Kafka handles events. Takes in needed info from sources. Stores information needed by any service for any CRUD operation.

## Technologies and Terms to Look up:
kafka ("event bus")
- <a href="https://youtu.be/Ch5VhJzaoaI?si=mpVnT6yKP2XiUSIS" target="_blank">Source</a>
- open source distributed event streaming platform
- good for things that need to stream data like locations in uber, messaging, or online games?
- puts events in queue. Later the events are consumed by consumers.
    - producer: what is causing the event (user doing something)
    - Queues are distributed over many machines by some logical Partition like a topic (distribute by game type)
        - Record: event in queue
            - Offset: uniquely identifies a Record in a Partition (queue). It is determined by topic and Partition number
        - Partition Key: thing that the queues are split on (like game type)
            - Partition Key is random if one is not specified
        - Broken: a machine holding Partitions
        - Topic: group of Partitions holding the same type of data (event type)
- Can create many duplicate consumers, working in parrallel and distributed on many machines
    - Consumers Group
        - Consumers have a Consumer Group Id which identifies what Consumer Group they are in, regardless of instance or which machine they are running on
- Resiliancy
    - Partitions are written in memory, so if a machine goes down, it can reboot and continue
    - duplicate Partitions are set up as a backup
        - Replcation Factor: number set to determine how many duplicate Partitions there will be
        - Each duplicate Partition is on a different Broker
- handles events

Http Poling: a few ways to get data (- latency)
- - <a href="https://youtu.be/ZBM28ZPlin8?si=ZGRNYujRxo227bZP" target="_blank">Source</a>
- Short Polling: (bad design) 
    - Client constantly makes requests to the Resource (server/service)
    - Resource will give and empty reponse or a payload like a JSON obj
    - Client may have object thats hooked up to the Resources respones
    - Good: if you have a really long delay in network calls. Also if the payload is small
    - Bad: constantly using resources on the Client and Resource 
- Long Polling: (good idea to use when there is little traffic)
    - Client will make a request to the Resource
    - Resource will keep the connection open, and respond with the payload when it is available.
    - Good: less resources. 
    - Bad: Tieing up a connection on both ends (how limited is the number of connections?) ? fault prone ? 
- Web Sockets: When you need low latency, or need to push updates to multiple clients (like in a chatroom)
    - A connection is established between the Client and Resource that is bidirectional
    - Resource controlls connection 
    - Resource send updates and information to Client when data becomes available or is updated on the backend
    - Good: Resource can send payloads to client as it sees fit
    - Bad: Tieing up a connection on both ends at all times

sharding database 
- shard id (primary key)

webhook

redis db

spark

Topic:
- redundancy (for failure)

