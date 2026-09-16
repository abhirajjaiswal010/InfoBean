UUID Module in Python

uuid is a built-in Python module used to generate Universally Unique Identifiers.

You don't need to install it.

import uuid
1. What is UUID?

A UUID is a 128-bit identifier designed to be extremely unlikely to collide with another UUID.

Example:

550e8400-e29b-41d4-a716-446655440000

Instead of using:

id = 101

you can use:

550e8400-e29b-41d4-a716-446655440000

This is especially useful for:

Database IDs
Users
Orders
Transactions
Files
API resources
Session IDs
Distributed systems

6. UUID Versions

Python supports several UUID generation methods.

Method	Purpose
uuid1()	Based partly on time and host information
uuid3()	Name-based, MD5
uuid4()	Random
uuid5()	Name-based, SHA-1
uuid6()	Time-ordered UUID
uuid7()	Time-ordered UUID using Unix timestamp
uuid8()	Custom-defined UUID

For your current learning level:

uuid1()
uuid3()
uuid4()
uuid5()

are enough to understand first.

For general application IDs, start with:

uuid.uuid4()