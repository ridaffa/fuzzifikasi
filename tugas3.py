import csv
import array
def itungNaik(x, a, b):
	return (x-a)/(b-a)

def itungTurun(x, c, d):
	return (-1*(x-d)/(d-c))

# def fuzzifikasi(arr, tipe, x, a, b):
	# if tipe == 'naik':
		# return itungNaik(x, a, b)
	# elif tipe == 'turun':
		# return itungTurun(x, a, b)
	# else:
		# 1
def itungLow(x, a, b):
	if x<=a:
		return 1
	elif x>a and x<b:
		return itungTurun(x, a, b)
	else:
		return 0
def itungMed(x, a, b, c, d):
	if x > a and x < b:
		if x >= c and x<=d:
			return 1
		else:
			if x<c:
				return itungNaik(x, a, c)
			if x>d:
				return itungTurun(x, d, b)
	else:
		return 0
def itungHigh(x, a, b):
	if x>=b:
		return 1
	elif x>a and x<b:
		return itungNaik(x, a, b)
	else:
		return 0
def fuzifikasi(x, batasBawahLow, batasAtasLow, batasBawahMed, batasAtasMed, batasAMed, batasBMed, BatasBawahHi, BatasAtasHi):
	arr = []
	arr.append(itungLow(x,batasBawahLow,batasAtasLow))
	arr.append(itungMed(x,batasBawahMed,batasAtasMed, batasAMed, batasBMed))
	arr.append(itungHigh(x,BatasBawahHi,BatasAtasHi))
	return arr;
	
# FUZZY RULE
# 				followerCount		LOW		MEDIUM		HIGH
# engagementRate

# LOW								N 		N			M

# MEDIUM							N 		M 			Y

# HIGH								N 		Y 			Y
def inferensi(fuzzFol, fuzzER):
	arrFol = []
	arrFol.append('low')
	arrFol.append('low')
	arrFol.append('low')
	arrFol.append('medium')
	arrFol.append('medium')
	arrFol.append('medium')
	arrFol.append('high')
	arrFol.append('high')
	arrFol.append('high')
	arrER = []
	arrER.append('low')
	arrER.append('medium')
	arrER.append('high')
	arrER.append('low')
	arrER.append('medium')
	arrER.append('high')
	arrER.append('low')
	arrER.append('medium')
	arrER.append('high')
	arr = []
	for x in range(0,9):
		n = []
		if arrFol[x] == 'low' and arrER[x] == 'low':
			n.append('no')
			n.append(min(fuzzFol[0],fuzzER[0]))
		if (arrFol[x] == 'low' and arrER[x] == 'medium'):
			n.append('no')
			n.append(min(fuzzFol[0],fuzzER[1]))
		if (arrFol[x] == 'low' and arrER[x] == 'high'):
			n.append('no')
			n.append(min(fuzzFol[0],fuzzER[2]))
		if arrFol[x] == 'medium' and arrER[x] == 'low':
			n.append('no')
			n.append(min(fuzzFol[1],fuzzER[0]))
		if (arrFol[x] == 'medium' and arrER[x] == 'medium'):
			n.append('maybe')
			n.append(min(fuzzFol[1],fuzzER[1]))
		if (arrFol[x] == 'medium' and arrER[x] == 'high'):
			n.append('yes')
			n.append(min(fuzzFol[1],fuzzER[2]))
		if arrFol[x] == 'high' and arrER[x] == 'low':
			n.append('no')
			n.append(min(fuzzFol[2],fuzzER[0]))
		if (arrFol[x] == 'high' and arrER[x] == 'medium'):
			n.append('yes')
			n.append(min(fuzzFol[2],fuzzER[1]))
		if (arrFol[x] == 'high' and arrER[x] == 'high'):
			n.append('yes')
			n.append(min(fuzzFol[2],fuzzER[2]))
		arr.append(n)
	inf = []
	maxNo = 0;
	maxMaybe = 0;
	maxYes = 0;
	for x in arr:
		if x[0] == 'no':
			if x[1] > maxNo:
				maxNo = x[1]
		if x[0] == 'maybe':
			if x[1] > maxNo:
				maxMaybe = x[1]
		if x[0] == 'yes':
			if x[1] > maxNo:
				maxYes = x[1]
	inf.append(maxNo)
	inf.append(maxMaybe)
	inf.append(maxYes)
	return inf

def defuzzifikasi(inferensi):
	yes = 100
	maybe = 70
	no = 50
	return ((inferensi[0]*no)+(inferensi[1]*maybe)+(inferensi[2]*yes))/(inferensi[0]+inferensi[1]+inferensi[2])
	
	
# def inferensi(arr[]):
	# for x in arr[]
arr = []
idx = 0
batasBawahLowFol = 10000
batasAtasLowFol = 20000
batasBawahMedFol = 15000
batasAtasMedFol = 40000
batasAMedFol = 30000
batasBMedFol = 35000
BatasBawahHiFol = 39000
BatasAtasHiFol = 90000

batasBawahLowER = 0.5
batasAtasLowER = 1
batasBawahMedER = 0.6
batasAtasMedER = 2.5
batasAMedER = 1.2
batasBMedER = 1.8
BatasBawahHiER = 2.2
BatasAtasHiER = 5


with open("influencers.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        isi = []
        isi.append(fuzifikasi(int(row['followerCount']), batasBawahLowFol, batasAtasLowFol, batasBawahMedFol, batasAtasMedFol, batasAMedFol, batasBMedFol, BatasBawahHiFol, BatasAtasHiFol))
        isi.append(fuzifikasi(float(row['engagementRate']), batasBawahLowER, batasAtasLowER, batasBawahMedER, batasAtasMedER, batasAMedER, batasBMedER, BatasBawahHiER, BatasAtasHiER))
        arr.append(isi)

fc = []
er = []
hasil_defuzzi = []
idx = 0;
for x in arr:
	for n in range(0,2):
		if n == 0:
			fc = x[n]
		else:
			er = x[n]
	duo = []
	duo.append(defuzzifikasi(inferensi(fc,er)))
	duo.append(idx)
	idx=idx+1
	hasil_defuzzi.append(duo)
hasil_defuzzi = sorted(hasil_defuzzi,key=lambda l:l[0], reverse=True)
no_record = []
for x in range(0,20):
	no_record.append(hasil_defuzzi[x][1])
for x in range(0,20):
	print(hasil_defuzzi[x])

with open('chosen.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["no_record"])
    writer.writerows(map(lambda x: [x], no_record))
