5 Steps
1. Define the problem space
- ask specific questions and get constraints - define the scope of the project
    - who are our customers
    - Do we need to interact with existing system?
    - reliability need
    - data consistence/freshness need
    - storage and bandwidth need
- **? Functional and Non-Functional Requirements ?**
    - **Functional Requirements: functions that a system must be able to do.**
        - "Features that directly fulfill the purpose of the system."
        - Features, workflows, user interactions
        - Actions that takes place: 
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


2. Design the System at a high level
- high level diagram of system
- ? 1 or more APIs for each system requirement ?
    - **! No which type of API to use and why !**
        - soap, rest, rpc, graphql?


3. Deep Dive into the design
- go into each component and talk about why you chose it for the design
    - data speed
    - data storage
    - load balancing
- **! Explain pros and cons !**


4. Identify bottlenecks and scaling opportunities
- how to improve robustness/resiliancy?
    - is there a single point of failure?
    - is data so important that we need duplicates stored elsewhere? if so, how important is it that the data is consistent?
- do we need to store data in country (maybe for legal reasons)
- is there peak times of usage
- how to scale system to support 10x more users?

Good to know:
- horizontal sharding
- cdn: content delivery networks
- caching
- rate limiting
- sql vs no sql databases

5. Review and Wrap up
- make sure your design covers all the requirements (although you should be doing this through the interview)

---

Avoid single point of failure: have backups (servers, data, etc)

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
Hash(req_id) -> 0<= hash < M
hash % n = server[i] that gets the request
```
- If this hashing occures with user data, then the same user will get routed to the same server.
    - This means we can save the user data in cache (ram) for faster response times.

## Consistent Hashing
- Servers are assigned *virtual nodes*
    - *virtual nodes* are points on *the ring*
- Requests are hashed and routed somewhere on the ring.
- The request get routed to the next virtual node on the ring, which then gets routed to the server (that the virtual node belongs too)


