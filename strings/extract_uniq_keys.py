test_list = [{'gfg' : 5, 'is' : 8, 'best' : 12},
  {'gfg' : 5, 'is' : 12, 'best' : 12},
  {'gfg' : 20, 'is' : 17, 'best' : 12}]

# printing original list
print("The original list is : " + str(test_list))
# initializing required keys
req_key1 = 'gfg'
req_key2 = 'best'
# Extract Unique value key pairs
# Using list comprehension
res = {tuple(sub[idx] for idx in [req_key1, req_key2]) for sub in test_list}
# printing result
print("The required values : " + str(res))