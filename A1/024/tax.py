year = int(input())
cc = int(input())

#ปีก่อน 1990 ถึง 1990 < 1500 cc
if year <= 1990 and cc <= 1500:
    print("1250")
#ปีก่อน 1990 ถึง 1990 > 1500 cc
elif year <= 1990 and 1500 < cc <= 2000:
    print("1400")
#ปีก่อน 1990 ถึง 1990  <2000 cc
elif year <= 1990 and cc > 2000:
    print("2000")

#1991-1999
if 1991 <= year <= 1999 and cc <= 1500:
    print("1100")
#ปี 1991-1999 <>1500 cc
elif 1991 <= year <= 1999 and 1500 < cc <= 2000:
    print("1300")
#ปี 1991-1999 <2000 cc
elif 1991 <= year <= 1999 and cc > 2000:
    print("1700")

#หลังปี 2000 cc<1500 cc
if year >= 2000 and cc <= 1500:
    print("1000")
#ปีก่อน 1990 ถึง 1990 > 1500 cc
elif year >= 2000 and 1500 < cc <= 2000:
    print("1200")
#ปีก่อน 1990 ถึง 1990  <2000 cc
elif year >= 2000 and cc > 2000:
    print("1500")
