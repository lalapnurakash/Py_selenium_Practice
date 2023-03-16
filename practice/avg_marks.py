if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name,*line = input().split()
        scores = list(map(float, line))

        student_marks[name] = scores
    query_name = input()

    output = list(student_marks[query_name])
    avg = sum(output) / len(output)
    print("%.2f" % avg)

    # 2
    # Harsh 25  26.5 28
    # Anurag 26 28 30
    # Harsh