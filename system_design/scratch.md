# 5 Steps for a System's Design Interview
## 1. Define the problem space
- ask specific questions and get constraints - define the scope of the project
    - Who are our customers?
    - Do we need to interact with existing system?
    - Reliability need
    - Data consistence/freshness need
    - Storage and bandwidth need
- **Functional and Non-Functional Requirements**
    - **Functional Requirements: functions that a system must be able to do.**
        - "Features that directly fulfill the purpose of the system."
        - Features, workflows, user interactions
        - Actions that take place: 
            - User must be able to create an account
            - Customer has to be able to make an order
            - System must be able to send an order confirmation to the user
    - **Non-Functional Requirements: Quality or <ins>performance</ins> or the system. Tech specs and performance standars.**
        - Performance, security, scalability, etc.
        - The System should be able to handle up to 1 million users concurrently (**scalability**)
        - It should load pages in under 2 seconds (**performance**)
        - Data should be encrypted during transmission (**security**)
        - The service should have 99.9% uptime (**availability**)
        - Low latency
        - High availability and scalability
        - Fault tollerance
        - How should the system handle failures?
        - Trade-offs:
            - Should we prioritize a faster response or more reliability?
    - Ask: **What are the most import features of this product/system?**
    - Ask: What is the average traffic volumn?
    - Make sure you found all the functional and non-functional requirements


## 2. Design the System at a high level
- high level diagram of system
- ? 1 or more APIs for each system requirement ?
    - **! Know which type of API to use and why !**
        - soap, rest, rpc, graphql?


## 3. Deep Dive into the design
- go into each component and talk about why you chose it for the design
    - data speed
    - data storage
    - load balancing
- **! Explain pros and cons !**


## 4. Identify bottlenecks and scaling opportunities
- How to improve robustness/resiliancy?
    - Is there a single point of failure?
    - Is data so important that we need duplicates stored elsewhere? if so, how important is it that the data is consistent?
- Do we need to store data in country (maybe for legal reasons)
- Are there peak times of usage
- How to scale system to support 10x more users?

Good to know:
- horizontal sharding
- caching
- rate limiting
- sql vs no sql databases

## 5. Review and Wrap up
- Make sure your design covers all the requirements (although you should be doing this through the interview)

---

# Avoid single point of failure: have backups (servers, data, etc)

? master-slave architecture ?

micro service architecture
- each service gets scaled at a different rate that (depending on need)

Distributed service  (partition)
multiple data centers 
- in case one goes down
- handle traffic quickly
^ load balancing will route traffic to different data center/kubernetes pods based on traffic and predicted response time

Decoupling the System (seperating concerns)

? Extensible ?

---

# Consistent Hashing
- Load Balancing
- **Load should be distributed evenly across all servers**

## Simple Hashing
```
n = num servers
Hash(req_id) -> 0 <= hash < M
hash % n = server[i] that gets the request
```
- If this hashing occures with user data, then the same user will get routed to the same server.
    - This means we can save the user data in cache (ram) for faster response times.

## Consistent Hashing
- Servers are assigned *virtual nodes*
    - *virtual nodes* are points on *the ring*
- Requests are hashed and routed somewhere on the ring.
- The request get routed to the next virtual node on the ring, which then gets routed to the server (that the virtual node belongs too)

---

# Message/Task Queue

- Priority Queue of tasks stored in memory. 
- Keeps track of which tasks are done.
    - Heartbeat to see what servers are still up.
        - if server goes down, the jobs the server was suppose to do will be redistributed to the rest of the servers.

- Examples of Message/Task Queues in the real world:
    - Rabbit MQ
    - Zero MQ
    - JMS (Java Messaging System)


---

# Monolith vs Micro Services Architecture
| Monolith | Micro Service |
|:----------:|:----------:|
| +Faster | +Easier to scale |
| +Less Complex | +Easier to develop features in parrallel |
| -Single point of failure (generally) | +Can scale individual features/services |
| -Harder to onboard | +Easier to onboard |
| -Harder to test (integration test) | |

* Microservices are generally used with large scale systems
* *If one microservice is only talking to one other micro service, then they should have been one service altogether.*

---

# Sharding Data
- When there is too much data and you need to access/query quickly
- Index the data, based on a hashed key
- **Data consistency is hard**
- Data availability is also difficult

- Joins are hard because you need to go across shards to get all the data
    
    - ? Use consistant hashing to get around this ?

If a shard gets too big. Break it down into smaller shards.
- This is handled by shard manager

Master-Slave
- All reads come from the slaves
- All writes go to the master
- If the master goes down, a new masters will be made out of the slaves

*Try NoSQL and Indexing before sharding*

---

# Caching
- "Reduce duplicate work by using memory."
- "Reduce latency with more storage."
- 3 Places to have cache
    1. Backend (db/server)
        - Store db results in cache on server
            - Like an in-memory hashmap
        - ? db has cache ?
    2. Frontend (client)
        - Cache results
    3. Global System, Cache Server
        - Redis
        - Interact with this cache server with get and post requests through an api
        - The benefit to this is that you can scale independently
    - All 3 of these options are used in the real world.
- ## Caching Policy
    - What to store in cache?
    - What, and when, to evict? (LRU, LFU, etc)
## Thashing:
- When many loads and evictions occure due to a bad caching policy.
- **Data consistency** how stale is the data in the cache.
    - **Eventual consistency**
        - When, and how often, do you update the cache?

---

# Single Point of failure
**Duplication** is a good way to get around this.
- duplicate *services* and *data*
    - Master-Slave: master gets write requests, slaves handle read requests
- Duplicate Load Balances (Gateways)
    - DNS will route to different load balancers
- Multiple regions in case an entire region goes down.
    - Also improves latency

**Backups**

**Master-Slave**

*Client failing is not as bad as a backend service failing (usually).*

---

# CDN
Load files you want to serve in cache. Have cache servers spread out to where your users are.

---
---

# Publisher Subscriber Model
- **Producer**: puts messages in the message broker
- **Subscriber**: subscribes/listens to certain messages from the message broker
## Benefits
* Decouple
    * Parent services can just give requests to the message broker, and if it's successfully added, it can respond with a 200 and move on to the next requests. The message broker will worry about sending it down stream
    * If a service is down, the 'message broker' will backoff and retry.
        * So parent services don't have to sit and wait for a child service to respond. This is useful when there are many child services downstream and maybe only 1 fails.
* Simplier
* More Scalable
    * You can remove/add services
    * Scale individual services
## Downsides
* Data Consistency
    * Hard to ensure data consistency across decoupled services.
        * So not good for financial services.

*Would be good for something like social media posts.*

- **Events Driven Services**
- **Message Broker**
    - a.k.a. **Event Bus**
    - **Kafka** is a popular example of an event bus
    - stores messages persistently

* Bases for *Event Driven Architecture*.

---

# Event Driven Architecture
* Used by: Git, React, Node.js, and games.
* Services save events in local db
* - Con: Data consistency
* + Pro: Easy roll back (In time b/c of events)
* + Pro: Easy replacement of services
    * New services subscribe to message broker
    * Transfer event db to new service
* Data intent is stored in the local event db
* - Con: Hidden flow
* - Con: Difficult to move out of (migrate)