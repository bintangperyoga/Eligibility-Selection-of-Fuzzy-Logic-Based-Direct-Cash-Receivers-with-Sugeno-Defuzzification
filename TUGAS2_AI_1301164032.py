# Nama    : Bintang Peryoga
# NIM     : 1301.1640.32
# Kelas     : IF-40-04

import csv

# 1. Linguistik
#     Pendapatan      R   S   T         skala 0 - 2
#     Hutang             D    B            skala 0 - 100
#     Acceptance      Y   M   N

# 2. Membership Function
    # terlampir di laporan

# 3. Fuzzyfication
def pendapatan(x):
    if x <= 0.5:
        r = 1
        s = 0
        t = 0
    elif x > 0.5 and x < 0.7:
        r = (x - 0.5)/(0.7 - 0.5)
        s = (x - 0.5)/(0.7 - x)
        t = 0
    elif x >= 0.7 and x <= 1.2:
        s = 1
        r = 0
        t = 0
    elif x > 1.2:
        t = 1
        r = 0
        s = 0
    return r, s, t

def hutang(y):
    if y < 50:
        d = 1
        b = 0
    elif y >= 50 and y <= 60:
        d = (y-40)/(60 - 40)
        b = (y - 50)/(70 - 50)
    elif y > 60:
        b = 1
        d = 0
    return d, b

# 4. Rule
# H\P       R       S       T
# D          M      N       N
# B           Y      M       N

# 5. Inference
def rules(r,s,t,d,b):
    maybe = []
    yes = []
    no = []
    maybe.append(-999)
    yes.append(-999)
    no.append(-999)

    if r == 1 and d == 1:
        maybe.append(1)
        yes.append(0)
        no.append(0)
    if r == 1 and b == 1:
        yes.append(1)
        maybe.append(0)
        no.append(0)
    if (r == 1 and 0 < d < 1) or (0 < r < 1 and 0 < d < 1) or (0 < r < 1 and d == 1):
        maybe.append(min(r, d))
        yes.append(0)
        no.append(0)
    if (0 < r < 1 and b == 1) or (0 < r < 1 and 0 < b < 1) or (r == 1 and 0 < b < 1):
        yes.append(min(r, b))
        maybe.append(0)
        no.append(0)
    if s == 1 and d == 1:
        no.append(1)
        maybe.append(0)
        yes.append(0)
    if s == 1 and b == 1:
        maybe.append(1)
        yes.append(0)
        no.append(0)
    if (s == 1 and 0 < d < 1) or (0 < s < 1 and 0 < d < 1) or (0 < s < 1 and d == 1):
        no.append(min(s, d))
        maybe.append(0)
        yes.append(0)
    if (0 < s < 1 and b == 1) or (0 < s < 1 and 0 < b < 1) or (s == 1 and 0 < b < 1):
        maybe.append(min(s, b))
        yes.append(0)
        no.append(0)
    if t == 1 and d == 1:
        no.append(1)
        maybe.append(0)
        yes.append(0)
    if t == 1 and b == 1:
        no.append(1)
        maybe.append(0)
        yes.append(0)
    return max(maybe), max(yes), max(no)

# 6. De-Fuzzyfication
#     batas NO = 65
#     batas MAYBE = 85
#     batas YES = 90
def sugeno(m, y, n):
    score = ((n*65)+(m*85)+(y*90))/(m + n + y)
    return score


#Program Utama
datafile = open("DataTugas2.csv", "r")
data = csv.reader(datafile)
arraydata = []
for row in data:
    arraydata.append(row)

score = []
for j in range(1,len(arraydata)):
    r, s, t = pendapatan(float(arraydata[j][1]))
    d, b = hutang(float(arraydata[j][2]))
    maybe, yes, no = rules(r,s,t,d,b)
    score.append([sugeno(maybe, yes, no),j])

score.sort(reverse=True)
op = []
op.append("ID")
for i in range(0,20):
    op.append(score[i][1])

# Test outputan ID/Nomor orang
# print("Daftar ID orang yang menerima BLT :")
# print(op)
# print("Banyaknya : ",len(op))

dataterima = open('TebakanTugas2.csv', 'w')
dataterimaa = csv.writer(dataterima)

for d in op:
    dataterimaa.writerow([d])

dataterima.close()