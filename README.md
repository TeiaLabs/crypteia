# crypteia

A crafty coder's content-addressing companion for cascading consistency checks with cryptographic cloak and charm in the cosmic chaos of cyberspace.

## usage

```python
from crypteia import Multibasing, Multihashing, ToBytes, compose

get_hash = compose(ToBytes(), Multihash("sha3-224"), Multibase("base58btc"))
data = "Hello, World!"
digest = get_hash(data)
print(digest)
# 'z5dbMfGzi9pjjDf5Uv7bVDqgPPMGAkrRDmEqSoVquB'
```

## validation

Multiformats use prefixes to indicate the encoding and hashing algorithms used.

```python
from annotated_types import Len, Predicate
from compose import compose  # pip install compose compose-stubs
is_base58btc_sha3224_string = compose(
    bool, re.compile(r"5dz[1-9A-HJ-NP-Za-km-z]{39}").fullmatch
)
HashDigest = Annotated[
    str,
    Len(42),
    Predicate(is_base58btc_sha3224_string),
]
```
