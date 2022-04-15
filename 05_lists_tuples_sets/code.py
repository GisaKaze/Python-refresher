l = ["Bob", "Rolf", "Anne"]
t = ("Bob", "Rolf", "Anne")
s = {"Bob", "Rolf", "Anne"}

# Access individual items in lists and tuples using the index.

print(l[0])
print(t[0])

l[0] = "Smith"

print(l)
print(t)
print(s)

# Add to a list by using `.append`

l.append("Jen")
print(l)
# Tuples cannot be appended to because they are immutable.

# Add to sets by using `.add`

s.add("Jen")
print(s)

# Sets can't have the same element twice.

s.add("Bob")
print(s)