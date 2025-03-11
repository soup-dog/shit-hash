# Shit Hash Specification
Shit hash is a hash function that always returns 42. Always.

## Shit Hash Package
### Name
The package name should consist of the words "shit" and "hash", once each, 
in that order. Capitalisation and word delimiters should match the 
implementation language. 

Examples of good package names meeting the spec:
- shit_hash
- shit hash
- Shit Hash
- shitHash
- ShitHash
  
### Contents
The package should expose a single function, detailed below.

### Testing
Encouraged, but not obligatory.

### Build Guide
Every package must include a build guide. Builds will be released via GitHub.

## Shit Hash Function
### Name
The function name should consist of the words "shit" and "hash", once each, 
in that order. Capitalisation and word delimiters should match the 
implementation language.

Examples of good function names meeting the spec:
- shit_hash
- shitHash
- ShitHash

### Parameters
A single parameter of the most generic type the implementation language offers. 
Ideally, a single implementation handles all possible datatypes in a language.
If this is not possible, overloads should be written that accept all base 
datatypes of the language.

The parameter should have a name appropriate to the implementation language.

Examples of good parameter names:
- obj (Python)

### Returns
42 as a 32 bit unsigned integer.


## Example Implementations
See the [python implementation](./python/README.md).
