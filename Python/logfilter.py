file = open('mtpi.hmi.log')
lines = file.readlines()
for line in lines:
    if line.find('FillHeadSubscriberRangeDecaying') > 1 or line.find('FillHeadReportBridge') > 1:
        print(line)