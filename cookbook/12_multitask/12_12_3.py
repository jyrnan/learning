def some_generator():
    result = yield data
    
f = some_generator()

result = None
while True:
    try:
        data = f.send(result)
        result = ...some caculation
    except StopIteration:
        break
