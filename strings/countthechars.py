a="the harry potter "
a=a.casefold()
substr="harry"
count={}.fromkeys(substr[:2],0)
for each in a:
     if each in count:
        #count=count.get(each)+1
        count[each]+=1
print(count)
