from bluetooth import *
from select import *

target_address = input("Paste target_address: ")
print("searching services of target_address ", target_address)

results = find_service(name = None, uuid = None, address = target_address)
for dict in results:
    for k,v in dict.items():
        print(k, v)
    input()
