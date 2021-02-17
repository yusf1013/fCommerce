n = 50
bat = open("run_" + str(n) + ".bat", "w")

for i in range(n):
    bat.write("start python likes.py " + str(i+1) + " " + str(n) + "\n")

bat.close()
