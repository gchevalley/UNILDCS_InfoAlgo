import odbchelper
print odbchelper.__name__
params = {"server":"test", "database":"greg"}
print odbchelper.buildConnectionString(params)
print odbchelper.buildConnectionString.__doc__