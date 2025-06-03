'''
test min function in a program:
'''

def main():
    a = [0,0,1]
    b = []
    b.append(float('inf'))
    b.append(float('-inf'))
    b.append(float('inf'))

    print("min(a): ", min(a))
    print("min(b): ", min(b))

if __name__=='__main__':
    main()
