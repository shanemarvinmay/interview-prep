# Vertical vs Horizontal Scaling

## Vertical Scaling: upgrade single computer (more memory, fast cpu/gpu, etc)
- Doesn't need load balancing
- Single point of failure
- Inter process communication (doesn't need to talk to other computers, since its all on one machine)
- Data consistency is way easier
- Hardware becomes limited  
## Horizontal Scaling: more machines
- Needs load balancing
- Resilient
- Inter network calls (rpc) between machines (? services ?)
- Data consistence is harder and more compliated 
- Hardware isn't nearly as limited