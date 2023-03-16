def UncommonWords(A, B):
 count = {}

 for word in A.split():
  count[word] = count.get(word,0)+1
  print(word,count.get(word,0)+1 )

# insert words of string B to hash
 for word in B.split():
   count[word] = count.get(word, 0) + 1
   print(word,count[word])

# return required list of words
 return [word for word in count if count[word] == 1]

# Driver Code
A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"

# Print required answer
print(UncommonWords(A,B))