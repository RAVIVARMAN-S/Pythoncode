def count_the_vowels(word):
    sum=0
    for i in word:
        if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
            sum=sum+1
    return sum #return sum values


word = input()
result=count_the_vowels(word) # Call the count_the_vowels function
print(result)


