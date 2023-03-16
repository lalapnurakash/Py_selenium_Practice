import bisect

days= { 'Mon', 'Tue', 'Wed','Thu'}
enum_days = enumerate(days)
print(type(enum_days))

# converting it to alist
print(list(enum_days))

# changing the default counter to 5

enum_days = enumerate(days, 6)
print(list(enum_days))
stack=bisect.bisect(list(days),'h')
print(stack)

