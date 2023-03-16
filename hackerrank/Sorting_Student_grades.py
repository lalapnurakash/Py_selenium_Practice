if __name__ == '__main__':
   def sort(elem):
    return (elem[1],elem[0])

if __name__ == '__main__':
    records= []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append((name,score))
        print("after adding",records)
# --sort based on the index (score) of records
#sorted(records, key=lambda record: record[1])

records=sorted(records,key=sort)
for i in range(1,len(records)):

    if  records[0][1]!=records[i][1]:
        try:
            if records[i][1]==records[i+1][1]:
                    print(records[i][0])
            else:
                print(records[i][0])
                break
        except IndexError:
            print(records[i][0])