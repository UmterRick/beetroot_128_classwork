set_a = {1, 2, 3, "a", "b", "c"}
set_b = {2, 4, 6, "c", "d", "e"}

diff = set_a.difference(set_b)
diff_2 = set_b.difference(set_a)
diff_alter = set_b - set_a

print("Diff A from B: ", diff)
print("Diff B from A: ", diff_2)
print("Alter Diff B with A: ", diff_alter)

print()


common = set_a.intersection(set_b)
common_2 = set_b.intersection(set_a)
alter_common = set_b & set_a

print("Common A with B: ", common)
print("Common B with A: ", common_2)
print("Common B with A: ", alter_common)
print()


set_c = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
set_d = {2, 4, 6, 8}

print(set_b.issubset(set_a))
print("D subset C: ", set_d.issubset(set_c))
print("C superset D: ", set_c.issuperset(set_d))


print(set_d.union(set_a))




