import csv
from operator import itemgetter
data = open("DataTugas2.csv","r")
data.readline()
pendapatan = []
hutang = []
fuzzyset1 = []
fuzzyset2 = []
fuzzyrules =[]
hasilsugeno = []
i = 0
nilai1 = float 
nilai2 = float	
nilai = float
status = ""
def grafikNaik (nilai,x,y): 
	hasil = (nilai-x)/(y-x)
	return hasil

def grafikTurun(nilai,x,y):
	hasil = (x-nilai)/(x-y)
	return hasil

def nilaiSugeno(status,nilai):
	if status == "high" :
		hasil = ((nilai * 90)) / (nilai)
	else :
		hasil = nilai * 70 /  nilai
	return hasil

for line in data :
	if line != "EOF" :
		splited = line.split(",")
		pendapatan.append(float(splited[1]))
		hutang.append(float(splited[2]))


for j in range(len(pendapatan)):	
	if pendapatan[j] <= 0.7 :
		nilai1 = 1 
		status1 ='rendah'
		nilai2 = 0
		status2 = 'rendah'
	elif pendapatan[j] > 0.7 and pendapatan[j] < 0.8 :
		nilai1= grafikNaik(pendapatan[j],0.7,0.8)
		status1='sedang'
		nilai2 = grafikTurun(pendapatan[j],0.7,0.8)
		status2='rendah'
	elif pendapatan[j] >= 0.8 and pendapatan[j] <= 1 :
		nilai1 = 1
		status1='sedang'
		nilai2 = 0
		status2='sedang'
	elif pendapatan[j] >1 and pendapatan[j]<1.5:
		nilai1 = grafikNaik(pendapatan[j],1,1.5)
		status1='tinggi'
		nilai2 = grafikTurun(pendapatan[j],1,1.5)
		status2='sedang'
	elif pendapatan[j] >=1.5:
		nilai1 = 1	
		status1 = 'tinggi'
		nilai2 = 0
		status2='tinggi'
	fuzzyset1.append([])
	fuzzyset1[j].append(status1)
	fuzzyset1[j].append(nilai1)
	fuzzyset1[j].append(status2)
	fuzzyset1[j].append(nilai2)


for j in range(len(hutang)):
 	if hutang[j] <= 20 :
		nilai3 = 1 
		status3 ='sedikit'
		nilai4 = 0
		status4 = 'sedikit';
	elif hutang[j] > 20 and hutang[j] < 35 :
		nilai3= grafikNaik(hutang[j],20,35)
		status3='sedang'
		nilai4 = grafikTurun(hutang[j],20,35)
		status4='sedikit'
	elif hutang[j] >= 35 and hutang[j] <= 60 :
		nilai3 = 1
		status3='lumayan'
		nilai4 = 0
		status4='lumayan'
	elif hutang[j] >60 and hutang[j]<75:
		nilai3 = grafikNaik(hutang[j],60,75)
		status3='banyak'
		nilai4 = grafikTurun(hutang[j],60,75)
		status4='lumayan'
	elif hutang[j] >=75:
		nilai3 = 1	
		status3 = 'banyak'
		nilai4=0
		status4='banyak'
	fuzzyset2.append([])
	fuzzyset2 [j].append(status3)
	fuzzyset2 [j].append(nilai3)	
	fuzzyset2 [j].append(status4)
	fuzzyset2 [j].append(nilai4)

for j in range(len(pendapatan)) :#kenapa menggambil range dari 
#len pendatapan agar perulanganya sama seperti banyak data 
	if (fuzzyset1[j][0] == 'rendah' and fuzzyset2[j][0] == 'sedikit' ):
		nilai=min(fuzzyset1[j][1],fuzzyset2[1])
		status='high'
	elif(fuzzyset1[j][0] == 'rendah' and fuzzyset2[j][0] == 'lumayan' ):
		nilai=min(fuzzyset1[j][1],fuzzyset2[1])
		status='high'
	elif(fuzzyset1[j][0] == 'rendah' and fuzzyset2[j][0] == 'banyak' ):
		nilai=min(fuzzyset1[j][1],fuzzyset2[1])
		status='high'
	elif (fuzzyset1[j][0] == 'sedang' and fuzzyset2[j][0] == 'sedikit' ):
		nilai=min(fuzzyset1[j][1],fuzzyset2[1])
		status='low'
	elif(fuzzyset1[j][0] == 'sedang' and fuzzyset2[j][0] == 'lumayan' ):
		nilai=min(fuzzyset1[j][1],fuzzyset2[1])
		status='low'
	elif(fuzzyset1[j][0] == 'sedang' and fuzzyset2[j][0] == 'banyak' ):
		nilai=min(fuzzyset1[j][1],fuzzyset2[1])
		status='high'
	elif(fuzzyset1[j][0] == 'tinggi' and fuzzyset2[j][0] == 'sedikit' ):
		nilai=min(fuzzyset1[j][1],fuzzyset2[1])
		status='low'
	elif(fuzzyset1[j][0] == 'tinggi' and fuzzyset2[j][0] == 'lumayan' ):
		nilai=min(fuzzyset1[j][1],fuzzyset2[1])
		status='low'
	elif(fuzzyset1[j][0] == 'tinggi' and fuzzyset2[j][0] == 'banyak' ):
		nilai=min(fuzzyset1[j][1],fuzzyset2[1])
		status='low'
	elif (fuzzyset1[j][0] == 'rendah' and fuzzyset2[j][2] == 'sedikit' ):
		nilai=min(fuzzyset1[j][1],fuzzyset2[3])
		status='high'
	elif(fuzzyset1[j][0] == 'rendah' and fuzzyset2[j][2] == 'lumayan' ):
		nilai=min(fuzzyset1[j][1],fuzzyset2[3])
		status='high'
	elif(fuzzyset1[j][0] == 'rendah' and fuzzyset2[j][2] == 'banyak' ):
		nilai=min(fuzzyset1[j][1],fuzzyset2[3])
		status='high'
	elif (fuzzyset1[j][0] == 'sedang' and fuzzyset2[j][2] == 'sedikit' ):
		nilai=min(fuzzyset1[j][1],fuzzyset2[3])
		status='low'
	elif(fuzzyset1[j][0] == 'sedang' and fuzzyset2[j][2] == 'lumayan' ):
		nilai=min(fuzzyset1[j][1],fuzzyset2[3])
		status='low'
	elif(fuzzyset1[j][0] == 'sedang' and fuzzyset2[j][2] == 'banyak' ):
		nilai=min(fuzzyset1[j][1],fuzzyset2[3])
		status='high'
	elif(fuzzyset1[j][0] == 'tinggi' and fuzzyset2[j][2] == 'sedikit' ):
		nilai=min(fuzzyset1[j][1],fuzzyset2[3])
		status='low'
	elif(fuzzyset1[j][0] == 'tinggi' and fuzzyset2[j][2] == 'lumayan' ):
		nilai=min(fuzzyset1[j][1],fuzzyset2[3])
		status='low'
	elif(fuzzyset1[j][0] == 'tinggi' and fuzzyset2[j][2] == 'banyak' ):
		nilai=min(fuzzyset1[j][1],fuzzyset2[3])
		status='low'
	elif (fuzzyset1[j][2] == 'rendah' and fuzzyset2[j][0] == 'sedikit' ):
		nilai=min(fuzzyset1[j][3],fuzzyset2[1])
		status='high'
	elif(fuzzyset1[j][2] == 'rendah' and fuzzyset2[j][0] == 'lumayan' ):
		nilai=min(fuzzyset1[j][3],fuzzyset2[1])
		status='high'
	elif(fuzzyset1[j][2] == 'rendah' and fuzzyset2[j][0] == 'banyak' ):
		nilai=min(fuzzyset1[j][3],fuzzyset2[1])
		status='high'
	elif (fuzzyset1[j][2] == 'sedang' and fuzzyset2[j][0] == 'sedikit' ):
		nilai=min(fuzzyset1[j][3],fuzzyset2[1])
		status='low'
	elif(fuzzyset1[j][2] == 'sedang' and fuzzyset2[j][0] == 'lumayan' ):
		nilai=min(fuzzyset1[j][3],fuzzyset2[1])
		status='low'
	elif(fuzzyset1[j][2] == 'sedang' and fuzzyset2[j][0] == 'banyak' ):
		nilai=min(fuzzyset1[j][3],fuzzyset2[1])
		status='high'
	elif(fuzzyset1[j][2] == 'tinggi' and fuzzyset2[j][0] == 'sedikit' ):
		nilai=min(fuzzyset1[j][3],fuzzyset2[1])
		status='low'
	elif(fuzzyset1[j][2] == 'tinggi' and fuzzyset2[j][0] == 'lumayan' ):
		nilai=min(fuzzyset1[j][3],fuzzyset2[1])
		status='low'
	elif(fuzzyset1[j][2] == 'tinggi' and fuzzyset2[j][0] == 'banyak' ):
		nilai=min(fuzzyset1[j][3],fuzzyset2[1])
		status='low'
	elif(fuzzyset3[j][2] == 'rendah' and fuzzyset2[j][2] == 'sedikit' ):
		nilai=min(fuzzyset3[j][3],fuzzyset2[3])
		status='high'
	elif(fuzzyset3[j][2] == 'rendah' and fuzzyset2[j][2] == 'lumayan' ):
		nilai=min(fuzzyset3[j][3],fuzzyset2[3])
		status='high'
	elif(fuzzyset3[j][2] == 'rendah' and fuzzyset2[j][2] == 'banyak' ):
		nilai=min(fuzzyset3[j][3],fuzzyset2[3])
		status='high'
	elif (fuzzyset3[j][2] == 'sedang' and fuzzyset2[j][2] == 'sedikit' ):
		nilai=min(fuzzyset3[j][3],fuzzyset2[3])
		status='low'
	elif(fuzzyset3[j][2] == 'sedang' and fuzzyset2[j][2] == 'lumayan' ):
		nilai=min(fuzzyset3[j][3],fuzzyset2[3])
		status='low'
	elif(fuzzyset3[j][2] == 'sedang' and fuzzyset2[j][2] == 'banyak' ):
		nilai=min(fuzzyset3[j][3],fuzzyset2[3])
		status='high'
	elif(fuzzyset3[j][2] == 'tinggi' and fuzzyset2[j][2] == 'sedikit' ):
		nilai=min(fuzzyset3[j][3],fuzzyset2[3])
		status='low'
	elif(fuzzyset3[j][2] == 'tinggi' and fuzzyset2[j][2] == 'lumayan' ):
		nilai=min(fuzzyset3[j][3],fuzzyset2[3])
		status='low'
	elif(fuzzyset3[j][2] == 'tinggi' and fuzzyset2[j][2] == 'banyak' ):
		nilai=min(fuzzyset3[j][3],fuzzyset2[3])
		status='low'
	fuzzyrules.append([])
	fuzzyrules[j].append(status)
	fuzzyrules[j].append(nilai)




for j in range(len(pendapatan)):
	hasilsugeno.append([])
	hasilsugeno[j].append(j+1)
	hasilsugeno[j].append(nilaiSugeno(fuzzyrules[j][0],fuzzyrules[j][1]))



hasilsugeno = sorted(hasilsugeno, key=itemgetter(1), reverse=True)

with open("TebakanTugas2.csv", 'w') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for i in range(20):
         wr.writerow([hasilsugeno[i][0]])
   