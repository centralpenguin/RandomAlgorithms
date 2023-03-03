from random import choice
from time import sleep

import time
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))


print("1 = Enrypt")
print("2 = Decrypt")
answer = (input("Insert ur answer: "))
if answer == "1":
    file_name = input("Key cwd: ")
    text = input("Message: ")
    encrypt = []; k = 0
    with open(file_name,"r") as file:
        read = file.read()
        for gg in read:
            temp = []
            for i,j in enumerate(read):
                if text[k] == j:
                    temp.append(i)
            try:
                encrypt.append(choice(temp)+1)
            except:
                pass
            finally:
                if k < len(text) - 1:
                    k += 1
                else:
                    break
    print("Crypted message")
    for i in encrypt:
        print(i, end="/")
    print()
elif answer == "2":
    file_name = input("Book-key name: ")
    keys = input("Crypted text: ")
    keys = [i for i in keys]
    encrypt = []; k = ""
    for i in keys:
        if i != "/":
            k += i
        else:
            encrypt.append(int(k)-1)
            k = ""
            continue
    decrypt = ""; k = 0
    with open(file_name,"r") as file:
        read = file.read()
        for gg in read:
            for i,j in enumerate(read):
                try:
                    if i == encrypt[k]:
                        if k <= len(encrypt) - 1:
                            k += 1
                            decrypt += j
                except:
                    break
    print("Decrypted message:\n" + decrypt)
else:
    print("Awkward")
sleep(100)