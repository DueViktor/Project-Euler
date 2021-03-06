import time
start = time.time()

def int_combinations(a_limit,b_limit):
    # Return a sequence of all linear combinations of 2 <= a <= a_limit and 2 <= b <= b_limit
    seq = set()
    a_,b_ = 2,2
    while a_ <= a_limit and b_ <= b_limit:
        for b_ in range(2,b_limit+1): seq.add(a_**b_)
        a_ += 1
    return seq

seq = int_combinations(100,100)

print("The number of distinct terms in the sequence generated by a**b are {}".format(len(seq)))
print("Time: {}".format(time.time()-start))