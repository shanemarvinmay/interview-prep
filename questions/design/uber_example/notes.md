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
* Horizontal Scaling: Using more machines and duplicates
* Vertical Scaling: Using more resources on one machine?

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
        - Broker : a machine holding Partitions
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
- <a href="https://youtu.be/ZBM28ZPlin8?si=ZGRNYujRxo227bZP" target="_blank">Source</a>
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

Sharding Database: Spliting database into logical sections on different machines
- <a href="https://youtu.be/XP98YCr-iXQ?si=Nb_MLFlrd5Js2zbT" target="_blank">Source</a>
- Data is replicated over several shards. 
    - So if one shard is lost...
        - you still have your data to serve
        - you don't permanently loose the data
- Reasons to use:
    - Good response time becaues there is less data to search through
    - Helps prevent total serice outages. 
    - You cannot continuosly vertically scale data. There is only some much storage space on a machine.
- Database is Sharded into Partitions
    - Logical Shard: database shard (partition)
    - Physical Shard: Node (machine)
    - Different Logical Shards run on different Nodes 
        - Nodes can have multiple Logical Shards
    - Shard Key: columns in database used to shard database
        - Shard Key can be a column in the table or a new one can be created
- "Shared-Nothing Architure": Physical Shards run indepentently and do no interact with eachother
    - This is the architecture type of a sharded database
    - Software Layer: abstract layer that is managing the Physical Shards
- Ways to shard:
    - Range-Based Sharding: bucketizing data based based on a range. An example should be, sharding users be the letter of their first name. One shard gets A-I, the next gets J-S, and the last gets T-Z.
        - One issue with Range-Based Sharding is that one bucket could get way more than the others
    - Hashed Sharding: bucketizing data based on a hash function that is performed on the row.
        - Good thing: This helps ensure that each shard is around the same size
        - Bad thing: Harder to scale (harder to change the logic to decide how the buckets should be chosen?) And the hash value doesn't represent any business logic.
    - Directory Sharding: Uses a look up table to decide what shard the row should go into. 
        - Good thing: This is very flexible
        - Bad thing: The look up table is the single point of failure. So if it is unavailable or wrong, then everything comes to a hault. (Why not just duplicate it then?)
    - Geo Sharding: Sharding data rows based on the location they are associated with. The data doesn't have to contain location information. It could simply be about a user in a certain region, or something like that.
        - Good thing: This enables low latency
        - Bad thing: The shards may not all be the same size. One shard may be much larger than the others..
- Database Hotspot: When one shard is overloaded (so this could mean other shards are underloaded). This defeats the purpoes of a sharded database.
    - Could occure when the Shard Key and Sharding method was poorly chosen.
- Cardinatity: How many possible values there are. So for booleans, the cardinality is 2.
    - This is something to consider when picking a Shard Key. You don't want a Shard Key that has too few possible values.
- Monotonic Change! It is good to think about how often your Shard Key can change.
    - For example if your Shard Key is the number of purchases a use makes, it will change frequently over time.
- Shard Key could be the primary key

webhook
- Opposite of api. API is you hitting a service, Webhook is you telling a service to hit you up when something happens.
    - so if you have a payment service like stripe. When a use checks out, the webhook you have set up with stripe will let you know when a transaction happens.

redis db: cache db instance running on RAM for speed
- Usefulness: hitting services then DB can be slow, RAM is fast. So data queried recently is stored in a Redis instance
- Multiple web servers can use 1 Redis instance running on a server
- Cache Miss: Client/User makes a request for data, but doesn't find it in the Redis db instance. So a request needs to be made to the db.
    - When a Cache Miss happens, the data is stored in the Redis db instance so this doesn't happen again.
- Cache Hit: Client/User makes a request for data, and quickly finds it in the Redis db instance.
- Cache Worker: monitors db for changes. When a change occures in the db, the Cache Worker stores a copy of that data in the Redis db instance.
- Ways to deploy a Redis instance:
    - Docker Container
    - Cloud Provider Managing your Redis instance (AWS, Azure, GCP)

Spark
- Processing big data that can't fit on one machine.

Topic:
- Redundancy (for failure)

EC2 (Elastic Compute Cloud)
- AWS Server.

exponential backoff
- if something goes wrong with a network request, you can retry the requestion over an over again with an exponentially increasing pause in between
    - 2 seconds pause after the first failure
    - 4 seconds pause after the third
    - the 8 seconds
    - and so on...