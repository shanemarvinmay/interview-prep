# Technologies and Terms to Look up:

Get requirements

! Trade off to decision making !

availability and consistency
- <a href="https://levelup.gitconnected.com/system-design-consistency-availability-and-cap-theorem-effb9326f8b5" target="_blank">No BS System Design: Consistency, Availability and CAP Theorem</a>
    - Consistency: When a write operation happens (client saves something, etc), that data needs to be able to be read and be the same as what was written. So if a client updates the'yre phone number, they should see the updated phone number everywhere.
        - one way to do this is in a distributed system, is Server 1 can replicated a write request to other servers before sending back an ACK (acknowledged) repsones.
    - Availability: Every request made by a client to an active server (is online, and isn't crashing) must respond eventually.
    - Partition Tollerance
        - Network Partition: (in this context) seems to mean, that X number of messages will get lost in our network.
        - Partition Tollerance: our system runs correctly despite Network Partitions taking place
    - CAP Theorem (Consistency Availability Partition Tolerance)
        - Applications (mainly distributed databases) can only guarantee 2 of the following three: Consistency, Availability, Partition Tolerance
        - Networks aren't perfect (Partition Tolerance is guaranteed) and reliable so you'll need to make software tradeoffs between Consistency and Availability
        - Consistency and Partition Tolerance choice: if a request to write some data is made, and network partition occures, then there is a time out and no data is written. This ensures the data is Consistent but doesn't guarantee Availability.
        - Availability and Partition Tolerance: "Eventual consistency"
            - This is where you make sure a node (server) is available regardless if it has the data needed. So the respones might have 'stale' data.
        - If the data integrity is of the highest priority: Consistency and Partition Tolerance is the way to go
        - If availibility (horizontal scaling) is the most import: Availability and Partition Tolerance
    - Consistency Patterns
        1. Weak Consistency: After data is written, read requests may or may not see the newest data. We just do our best.
            - This is often done, in most cases, as a cache. 
            - This is usually a good idea when it's not critical that the data being read is correct. So video chat, multiplayer games, and VoIP (internet) calls are all good examples of this.
        2. Eventual Consistency: A bunch of asynchronous requests to update the other node's data are made. This makes the data *eventually* consistent.
            - This works well with systems that need to be highly available like; email, search engines, and dns.
        3. Strong Consistency: After a write, all reads will get the newest data.
            - Data is replicated synchronously. (No moving on until everyone is one the same page.)
            - Useful wehn systems need transactions like file systems (cloud and local), RDBMS, and maybe financial transactions?
    - Availability Patterns
        - Fail-Over
            1. Active Passive Fail-Over
                - "Active" servers handle traffice
                - Passive servers are ready to jump in if needed (standby)
                - A heartbeat is sent out between active and passive servers. If the heart beat is interupted, the passive server takes over and starts handling traffic
            2. Active-Active Fail-Over
                - All servers are active and load is shared between them.
                - If servers are public facing, DNS needs to know the IP of both of them
                - If the servers are interal facing, the app needs to know their IP
            Disadvantages of Fail-Over
                - Additional hardware and complexity
                - Data could be lost if an active server fails before the data didn't permeate.
        - Replication
            - Active Passive Replication: ? more servers are pulled in (come online) if needed ?
            - Active Active Replication: ? more active servers come onlin if needed ?
              

# Polling vs Streaming
## Long and Short Polling
(See uber_example Http Polling notes)
## Server Sent Events (SSE)
- Client makes a request to a server and makes a "connection"
    -"connection" is basically saying "heres my address, send me updates"
- After initial "connection" is made, data only flows from the server to the client
- Server then sends updates to the clients as they occure 
- Eventualy the server will send a final message canceling the "connection"
- ! Can only have 6 connections to a client !
- Done with http like polling (short and long)
## WebSockets
- Handshack occures between the client and the server over http. Addresses are exchanged
- Then TCP messages can be quickly sent back and forth between the client and the server
    - Port 443 is used (80 if not TLS encrypted)
- Really fast (good for gaming)
- ! Firewalls sometimes block the ports needed for websockets !
### Different than webhooks!
- webhooks is when a service has an address that doesn't change
- webhooks send information in one direction.
## Streaming
- encoder
- RTMP (Real-Time Messaging Protocol)
    - TCP based protocol
    - RTMPS: the S stands for secure
- SRT (Secure Reliale Transport)
    - new, and could replace rtmp
    - udp based and not tcp
    - lower latency than 
    - generally not supported yet.
- PoP Server (Point-of-Presence)
    - ? server that processes and packages the video ?
    - stream quality to determined
    - segmentation: video broken into couple second chunks
    - packages segments into:
        - HSL (HTTP Live Streaming)
            - most popular
            - manifest file says what order the segments go in
            - video segments go with the file
        - DASH (Dynamic Adatpive Streaming over HTTP)
    - packages are cached along the way


? messaging patterns ?

asynchronism (I think I know it)

# load balancing (just skimmed it)
- round robin
- least load
- url ip hashing

# caching
- clients
- servers
- in memory
- dedicated caching service like redis
- eviction policy
- cnd
- what info will be stored
## info notes
- top non functional requirement goals
    - scalability
    - availability
    - performance (speed)
    - durability (if you need to save data)
- Least Recently Used Cache
    - local cache
        - hash table in memory
    - eviction policy ! (to ensure hashtable doesn't fill up)
        - aka Replacement Policies
        - least recently used policy: remove oldest data
            - queue, to keep track of newest and oldest data
                - doubly linked list
                - Implimentation is in screenshot in this dir
    - distributed cache
        - Share cache with some logical partition
        - Dedicated Cache Cluster: services and cache shards are on different hardward
            - benefit: services and caches can scale independently 
        - Co-Located Cache: services and cache shards share hardware.
            - benefit: saves on hardware cost
- hashing
    - MOD hashing: the hashing you used when building a hashtable
        - issue with caching: what happens when a shard goes down or gets added? this could cause services to hit the wrong caches and result in many cache misses.
    - ! Consistent hashing ! : hashing something constant, like IP address. Then everything in range from some-ip's hash and the next hash, belong to that ip address. (pic in this dir to help explain)
        - Issues !
            - when a Cache Server goes down, all of its load is dumped onto the next Cache Server
            - hashes don't ensure that each Cache Server has the same load. One Cache Server might end up with 90% of the load
- Cache Client
    - live in service
    - knows about all Cache Servers (shards)
        - all Cache Clients will know about all Cache Servers
    - address of Cache Servers are stored in sorted order by hash value
        - like in a tree map
    - binary search it usd to find the right Cache Server to use
    - TCP or UDP are used to talk to Cache Servers
    - if Cache Server is unavailable, client proceeds as if it was a cache miss
        - Resiliant
    - How Cache Clients know about Cache Servers
        1. ip address of Cache Servers are stored in storage.
            - Cache Client then queries storage to get current list
        2. Configuration Service: is a services that keeps track of Cache Servers.
            - Cache client reaches out to Configuration Service to find the right Cache Server
            - Configuration Services get heartbeats from Cache Servers to make sure they are available
            - benefit: this helps us find new Cache Servers as they come
            - benefit: if a Cache Server dies or is taken down, the Configuration Services will redirect as needed
- High availability (durability)
    - Leader-Follower
        - Leader handles put requests, and so, has data
        - Followers do their best to be replicas of the leaders.
        - Followers handle get requests.
        - illustration in this dir.
- Consistency vs Availability:
    - caches are focused on providing speed so availability will be prefered over consistence
        - consistency issue (in Leader-Follower) since Followers handle only get requests, they might not have the latest data the Leader has. So the data might be old.
- Data Expiration:
    - if cache never fills, should the data stay in there forever
        - might want to consider a TTL policy
- check local cache, if miss, check cache server
- security. set up firewall so only approved clients can access ports on cache server
    - encrypt and decrypt data
- monitor and logging
    - latency
    - caches hits and misses


? Daemon process ? 

consistent hashing

databases
- sql vs no sql 
    - benefit of one over the other
- sharding
- replication
- indexing

look up design interviews
- could start with where they design...
    - facebooks
        - facebook news feed
    - google drive
    - google search
    - whatsapp
    - amazon
    - netflix

high level overview first, then dive down

youtue resources
- gaurav sen 
- tech dummies narenda l

Grikking the system design interview - not free

algo expert - not free

-------------

gradient descent

bias / variance trade off
- bias: how far off the model typicaly is
- variance: how big the spread of model output is
- model complexity (num of basis functions) effects the balance between bias and variance
    - more complexity means more variance and less bias
        - ? overfitting ?
    - simplier model means more bias and less variance
        - ? underfitting ?
- find a balance for the best model is most cases

no labels, what do you do
- supervised learning
- vialize data to gain insight

confusion matrix (error matrix)
- tp, fn
- f1 scores (f measure, f score)
    - ```2 * (precision * recall) / (precision + recall) ```
    - balance between precision and recall
    - good for imbalanced datasets
- accuracy: how correct is the model overall
    - useful when classes are blanced, but maybe not if you want your model to predict something that isn't balanced. like spam, 90% emails are not spam, so the real world data isn't balanced.
        - so if the model just always said the email wasn't spam, the accuracy would look GREAT! but it could also be just saying everything isn't spam and still getting the 90%
    - ``` correct predictions / all predictions ```
    - ``` (TP + TN) / (TP + TN + FP + FN)```
- precision: how good the model is at predicting a class. This class can be a bool and could be how many of the yes's are true
    - good at looking how one class is predicted
    - good for unbalanced datasets
    - useful when the cost of FP is high
        - you want to be more precision, even if you miss a few
    - Doesn't account for FN, so we don't know how much we are missing out on
    - ``` TP / (TP + FP)```
- recall
    - ``` TP / (TP + FN)```
    - useful with unbalanced datasets
    - uesful with the cost of missing TP (or getting a FN) is high
    - downside, you don't account for FP. So saying YES everytime will give you 100% recall but everything else will be terrible


outliers and anoymolies
- outlier is uncommon but still part of the bell curve of your data. Uncommon, but still expected sometimes
- anomoly: you would really never expected it

? knn ?
- supervised classifier that isn't a parametric line
- uses proximity to make predictions (clusters)

grid search
- how to find hperparameters

Behavorial

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

meeting vs work

stack: what tools are being used for the project

bringing in model I build
- or new idea
- who do I give it too

any big technical challenges the team is faceing
- i know this project is needing to be migrated, but besides that

mobility apple

worst part of apple
- What is something you wish were different about your job?

What is unique about working at this company that you have not experienced elsewhere?

most important attribute of an ideal canidate

what does ramp up look like on the team

What are the strengths and weaknesses of the current team? What is being done to improve upon the weaknesses?

```````````````````````````````````````````````````````````
decision tree is easier to understand over nueral network

pep8 python style guide