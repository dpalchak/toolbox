## General ##

* Restrict use of function overloading to functions called in generic (aka template) situations.
Prefer unique names for unique operations, including unique names for different argument counts.
Don't use default arguments.

* std::endl also flushes output. Prefer '\n' instead.

* std::memcpy can be elided by compiler in some cases. This is a better option than reinterpret_cast

* Use `if constexpr` rather than std::enable_if and other template-based programming techniques

* Use friend functions for ADL-based injection of operators (and other useful helper functions)

* Prefer traits classes for very type-specific customization points; prefer ADL for more general
customization points


## Tricks ##
* Use structured binding syntax to get elements of aggregates without knowing element names

* Use base class to provide strorage for value(s) to make aggregate initialization easier

* Use std::overload to inherit a collection of overloaded operators (such as with lambdas)

*

## References

* `struct` based strong typing with operations as mixin classes:
https://github.com/PeterSommerlad/PSsst

* Forward declarations for libstdc++:
https://github.com/olegpublicprofile/stdfwd




