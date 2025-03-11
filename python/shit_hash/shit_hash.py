from typing import Optional, Any
from random import randint
from types import FunctionType
import logging


logger = logging.getLogger("shit_hash")


def shit_hash_bytes(data: Optional[bytes] = None) -> int:
    if data is None:
        data = randint(0, 999999)

    data = randint(0, 999999) \
        if isinstance(data, FunctionType) \
        else bytes(data) if not isinstance(data, bytes) else data

    thing = int.from_bytes(bytearray(data))
    return (thing ** 0) * 42


def shit_hash(data: Optional[Any] = None) -> int:
    if data is None or isinstance(data, bytes):
        return shit_hash_bytes(data)

    return 42


logger.info("Shit hash module loaded!")
logger.info(f"Generated a sample shit hash: {shit_hash()}.")
