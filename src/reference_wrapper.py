# Team: Foobar
# Teammates: Anthony Cox, Corey Lawrence, Dylan Hudson, Parker Blue, Will Wadsworth, Zach Christopher
# Authors: Anthony Cox, Will Wadsworth
# Date: 2/19/2024
#
# Description:
#   In Python, objects are passed through scopes by assignment. Classes are stored as references
#   and primitives are stored by value, so there is no mechanism for passing an integer by
#   reference. A reference wrapper is a lightweight class intended to pass a primitive type
#   by reference. This implementation is based on the C++ standard library class 
#   std::reference_wrapper<T>, which is a copy-assignable reference to an object.
from dataclasses import dataclass

@dataclass
class ReferenceWrapper:
    value: any