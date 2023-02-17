N = int(input("Введите кол-во слов: "))
s = str("")
word = str("")
for i in range (N):
    word = input("Введите слово: ")
    s = s + " " + word
print(s)