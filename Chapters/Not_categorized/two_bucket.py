def measure(bucket_one, bucket_two, goal, start_bucket):
    visited = set()
    queue = []

    if goal > bucket_one and goal > bucket_two:
        raise ValueError("No Solution Possible")

    if start_bucket == "one":
        queue.append((bucket_one, 0, 1))
        invalid = (0, bucket_two)

    else:
        queue.append((0, bucket_two, 1))
        invalid = (bucket_one, 0)

    while queue:
        b1, b2, step = queue.pop(0)
        if b1 == goal: return step, 'one', b2
        if b2 == goal: return step, 'two', b1

        if (b1, b2) in visited or (b1, b2) == invalid:
            continue
        visited.add((b1, b2))

        # Pouring one bucket into the other bucket until either: a) the first bucket is empty b) the second bucket is full
        queue.append((min(b1 + b2, bucket_one), b2 - (min(b1 + b2, bucket_one) - b1), step + 1))
        queue.append((b1 - (min(b1 + b2, bucket_two) - b2), min(b1 + b2, bucket_two), step + 1))

        # Emptying a bucket and doing nothing to the other.
        queue.append((b1, 0, step + 1))
        queue.append((0, b2, step + 1))

        # Filling a bucket and doing nothing to the other.
        queue.append((bucket_one, b2, step + 1))
        queue.append((b1, bucket_two, step + 1))

    raise ValueError("No Solution Possible")

'''
Instructions
Given two buckets of different size and which bucket to fill first, determine how many actions are required to measure an exact number of liters 
by strategically transferring fluid between the buckets.

There are some rules that your solution must follow:

You can only do one action at a time.
There are only 3 possible actions:
Pouring one bucket into the other bucket until either: a) the first bucket is empty b) the second bucket is full
Emptying a bucket and doing nothing to the other.
Filling a bucket and doing nothing to the other.
After an action, you may not arrive at a state where the initial starting bucket is empty and the other bucket is full.
Your program will take as input:

the size of bucket one
the size of bucket two
the desired number of liters to reach
which bucket to fill first, either bucket one or bucket two
Your program should determine:

the total number of actions it should take to reach the desired number of liters, including the first fill of the starting bucket
which bucket should end up with the desired number of liters - either bucket one or bucket two
how many liters are left in the other bucket
Note: any time a change is made to either or both buckets counts as one (1) action.

Example: Bucket one can hold up to 7 liters, and bucket two can hold up to 11 liters. Let's say at a given step, bucket one is holding 7 liters 
and bucket two is holding 8 liters (7,8). If you empty bucket one and make no change to bucket two, leaving you with 0 liters and 8 liters respectively (0,8), 
that counts as one action. Instead, if you had poured from bucket one into bucket two until bucket two was full, resulting in 4 liters in bucket one and 
11 liters in bucket two (4,11), that would also only count as one action.

Another Example: Bucket one can hold 3 liters, and bucket two can hold up to 5 liters. You are told you must start with bucket one. 
So your first action is to fill bucket one. You choose to empty bucket one for your second action. For your third action, you may not fill bucket two, 
because this violates the third rule -- you may not end up in a state after any action where the starting bucket is empty and the other bucket is full.
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/two-bucket/canonical-data.json
