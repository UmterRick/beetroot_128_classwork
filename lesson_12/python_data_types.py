# tuple VS set
from attr.setters import frozen

# tuple/list - store elements of diff types
# dict / set - store hashable types as keys

# list/dict/set - mutable
# tuple/frozenset - immutable


tuple_1 = (1, 2, 2, "jnds", True, None, {"key": "value"}, {1, 2, 3, 4, 4, 4})
set_1 = {1, 2, 2, "jnds", True, 1,  None, frozenset((1, 2, 33, 33, 2))}

print("Tuple: ", tuple_1)
print("Set: ", set_1)
frozen_set_1 = frozenset((1, 2, 33, 33, 2))


