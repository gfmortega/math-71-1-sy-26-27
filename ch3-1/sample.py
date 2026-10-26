import time

start_t = time.time()
A = []
for i in range(10**6):
    # A.append(i)
    A.insert(0, i)

end_t = time.time()

print(sum(A))
elapsed_t = end_t - start_t
print(f"time: {elapsed_t:.16f}s")
