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

http poling (- latency)

web sockets 

sharding database 
- shard id (primary key)

webhook

redis db

spark

Topic:
- redundancy (for failure)

