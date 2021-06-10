

# 40P
# 2) Get from input two different times in the format dd:hh:mm:ss and print the difference between them in the
# received format dd:hh:mm:ss
# dd is number of days
# hh is number of hours (00-23)
# mm is number od minutes (00-59)
# ss is number of seconds (00-59)

time1=input("Enter the time1\nType here:")
time2=input("Now enter the time2\nType here:")
dd1 = int(time1[:2])
hh1 = int(time1[3:5])
mm1 = int(time1[6:8])
ss1 = int(time1[9:])

dd2 = int(time2[:2])
hh2 = int(time2[3:5])
mm2 = int(time2[6:8])
ss2 = int(time2[9:])

t1 = 86400 * dd1 + 3600 * hh1 +  60 * mm1 + ss1
t2 = 84400 * dd2 + 3600 * hh2 +  60 * mm2 + ss2
print ('time difference:', t2 - t1)

