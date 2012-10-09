d = {"server":"mpilgrim", "database":"master","uid":"sa","pwd":"secret"}
print(d)
print(d["server"])
print(d["database"])
"""print(d["mpilgrim"])"""

d["database"] = "pub"
print(d)

d["key"] = "key"
d["Key"] = "Key"
d["retrycount"] = 3
d[42] = "douglas"
del d["server"]
print(d)