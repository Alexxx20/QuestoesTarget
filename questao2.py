def procurarFibonacci(num) -> bool:

    if num == 0:
        return True
    if num == 1:
        return True

    fibNumber = 1
    lastNum = 1

    while num >= fibNumber:

        if fibNumber == num:
            return True
        
        lastNum, fibNumber = fibNumber, fibNumber+lastNum

    return False

num = int(input('Qual número você quer procurar na sequência de Fibonacci? '))

if procurarFibonacci(num):
    print('O número está da sequência de Fibonacci')

else:
    print('O número está da sequência de Fibonacci')