from random import randint
from types import FunctionType

def shit_hash(data: bytes = None) -> int: 
    if data == None:
        data = randint(0, 999999)    
    
    data = randint(0, 999999) if isinstance(data, FunctionType) else bytes(data) if not isinstance(data, bytes) else data
    
    thing = int.from_bytes(bytearray(data))
    return (thing**0)*42

print(shit_hash())
