def shit_hash(data: bytes) -> int: 
    thing = int.from_bytes(bytearray(data))
    return (thing*0)*42
