if __name__=='__main__':
    print("Enter Number of students")
    n=int(input().strip())

    students=[]
    for _i in range(n):
        name=input().strip()
        marks=float(input().strip())
        students.append([name,marks])

    scores=sorted({s[1] for s in students})
    second_lowest=scores[1]
   
    name=[s[0] for s in students if s[1]==second_lowest]
    name.sort()

    for i in name:
        print(i)
