# Can I beat Redis?
Of course, I can't. Redis is a magical piece of code written in C.

## What is this about then?
Inspired by this Quora Haqaton challenge, I've implemented a sorted set datastore similar to Redis in python.
The goal here is benchmark things. 
* If my datastore is slower the Redis (maybe it isn't), how much slower? 
* Which are the bottlenecks?
* Can I get mine faster by using PyPy? Writing extensions in C? How faster?
