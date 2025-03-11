# Shit Hash Specification
Specification for the implementation of shit hash.

## Name
The function name should consist of the words "shit" and "hash", once each, 
in that order. Capitalisation and word delimiters should match the 
implementation language.

Examples of good function names meeting the spec:
- shit_hash
- shitHash
- ShitHash

## Parameters
A single parameter of the most generic type the implementation language offers. 
Ideally, a single implementation handles all possible datatypes in a language.
If this is not possible, overloads should be written that accept all base 
datatypes of the language.

The parameter should have a name appropriate to the implementation language.

Examples of good parameter names:
- obj (Python)

## Returns
42 as a 32 bit unsigned integer.


## Example Implementations
See the [python implementation](./python/README.md).
