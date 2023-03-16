# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     arr=list(arr)
#    # arr.sort()
#
# second_max=arr[0]
# first_max=arr[0]
# for ar in arr:
#     if first_max<ar:
#         second_max=first_max
#         first_max=ar
#
# print(second_max)
# print(first_max)

# if __name__ == '__main__':
#     n = int(input())
#     arr = list(set(map(int, input().split())))
#     arr.remove(max(arr))
#     print(max(arr))

''' to get the same scored names in order '''


if __name__ == '__main__':

    totalList = []
    listScore = []


    def getSecondLowestScore(listScore):
        listScore = sorted(list(set(listScore)))
        return (listScore[1])


    def getStudentList(totalList, score):
        finalList = [x for x, k in totalList if k == score]
        print(*(sorted(finalList)), sep='\n')


    for _ in range(int(input())):
        name = input()
        score = float(input())
        listScore.append(score)
        totalList.append([name, score])

    getStudentList(totalList, getSecondLowestScore(listScore))