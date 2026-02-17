import time
a = 0
print ("Hacking Pentagon...")
while a < 100:
    a += 5
    print ("Hacking pentagon complete in... ", a, "%" )
    time.sleep(1)
    if a == 100:
        print("Hacking Pentagon Sucessfuly!")
        exit()
