def checkPrimeNum():
    num = int(input("Enter the Number :"))
    count = 0
    for i in range(1,num+1):
        if num % i == 0 and num % 1 == 0:
            count+=1      
    if count <= 2:
        print(f"The Provided Number {num} is Prime number")
    else:
        print(f"The Provided Number {num} is Not Prime number")


checkPrimeNum()
