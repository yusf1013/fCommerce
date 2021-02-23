n = 100
bat = open("run_" + str(n) + ".bat", "w")

for i in range(n):
    bat.write("start python likes.py " + str(i+1) + " " + str(n) + "\n")
    bat.write("ping 127.0.0.1 -n 11 > nul\n")

bat.close()
