from collections import deque
queqe = deque ([])
queqe.append(1)
queqe.append(2)
queqe.append(3)

queqe.popleft()
print (queqe)

if not queqe:
    print("empty")