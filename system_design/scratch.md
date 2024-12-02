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
    - dast storage
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

vertical scaling: upgrade single computer (more memory, fast cpu/gpu, etc)
- doesn't need load balancing
- single point of failure
- inter process communication (doesn't need to talk to other computers, since its all on one machine)
- data consistency is way easier
- hardware becomes limited  
horizontal scaling: more machines
- needs load balancing
- resilient
- Inter network calls (rpc) between machines (? services ?)
- data consistence is harder and more compliated 
- hardware isn't nearly as limited

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


extensible