

def new_progression(N):
    temp = []
    for n in range(1, N+1):
        temp.append ((1+1/n)**n)
    return temp

numb = new_progression(int(input("Введите n:")))
print(sum(numb))
