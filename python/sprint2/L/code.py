import sys


class Node:
    def __init__(self, value, prev1=1, prev2=1):
        self.items = [1, 1]
        self.value = value
        self.prev1 = prev1
        self.prev2 = prev2


class Stack:
    def __init__(self):
        #self.items = []
        #self.max = None
        self.prev1 = 1
        self.prev2 = 1

    def push(self, item):
        #item = Node(item, None)
        #self.prev2, self.prev1 = self.prev1, self.prev1 + self.prev2
        self.prev2, self.prev1 = 1, 2

    def print_value(self):
        return self.prev1

    def pop(self):
        if not self.items:
            print("error")
            return "error"
        self.max = self.items.pop().max_value
        return

    def get_max(self):
        if not self.items:
            return None
        return self.max

#def fib(n):
#    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
#    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
#        calc = v2*v2
#        print(bin(n), rec)
#        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
#        if rec == '1':
#            v1, v2, v3 = v1+v2, v1, v2
#    return v2


def solution(n):
    #student_res = 1
    ##lst = [None] * (n + 1)
    #lst = [0, 1]
    #lst[0] = 1
    #lst[1] = 1
    #if n == 0 or n == 1:
    #    return student_res
    #i = 1
    #student1 = 1
    #student2 = 1
    #dct = {0: 1, 1: 1}
    stack = Stack()
    for i in range(2, n + 1):
        stack.push(i)
    return stack.print_value()
    #    #dct.update({i: dct[i - 1]})
    #    lst.append(lst[i - 1] + i)
    #    #print(lst[i - 1], lst[i - 2])
    #    #lst[i] = lst[i-1] + lst[i-2]
    ##for i in range(n-1):
    ##    student_res = student1 + student2
    ##    student2 = student1
    ##    student1 = student_res
    #return lst.pop()


def read_input():
    n, m = map(int, sys.stdin.readline().strip().split())
    return n, m


def main():
    n, m = read_input()
    result = solution(n)
    #result = fib(n+1)
    #print(result % 10 ** m)
    print(result % 10 ** m)


if __name__ == "__main__":
    main()

