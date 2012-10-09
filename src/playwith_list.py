li = ["a", "b", "mpiligrim", "new", "new", "z", "example"]
print(li)
print(li[0])
print(li[4])
print(li[-1])
print(li[-3])

print(li[1:3])
print(li[1:-1])
print(li[0:3])
print(li[:3])
print(li[3:])

print(li)
li.append("new withtout param so at the end")
print(li)
li.insert(2,"new with indice")
print(li)
li.extend(["extend first two", "extend second element"])
print(li)

print(li.index("example"))
"""print(li.index("c"))"""
print("z" in li)
print("c" in li)

li.remove("z")
print(li)
li.remove("new")
print(li)
print(li.pop())
print(li)

li = ["a", "b", "mpiligrim"]
print(li)
li = li + ["example", "new"]
print(li)
li += ["two"]
print(li)

li = [1,2] *3
print(li)