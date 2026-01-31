if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *scores = input().split()
        student_marks[ name ] = list(map(float, scores))

    query_name = input()

    total = 0
    for mark in student_marks[ query_name ]:
        total += mark

    avg = total / len(student_marks[ query_name ])
    print(f"{avg:.2f}")