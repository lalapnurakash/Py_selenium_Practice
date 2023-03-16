test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'
print("The original string is : " + str(test_str))

# Words Frequency in String Shorthands
# Using dictionary comprehension + count() + split()
res={}
for key in test_str.split():
   #  res = {key: test_str.count(key) for key in test_str.split()}
   res.__setitem__(key,test_str.count(key))
# printing result
print("The words frequency : " + str(res))