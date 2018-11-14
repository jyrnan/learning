import concurrent.futures

# A fucntion that perform a lot of work
def work(x):
    # do some work here
    return result


# Nonparallel code
results = map(work, data)

# Parallel implemention
with concurrent.futures.ProcessPoolExecutor() as pool:
    results = pool.map(work, data)

with concurrent.futures.ProcessPoolExecutor as pool:
     # Example of submitting work to the pool
    future_result = pool.submit(work, arg)

     # Obtaining the result from (blocks untill done)
     r = future_result.result()

# 还可以添加一个回掉函数来获取结果
def when_done(r):
    print('Got:', r.result())


with concurrent.futures.ProcessPoolExecutor() as pool:
    future_result = pool.submit(work, args)
    future_result.add_done_callback(when_done)