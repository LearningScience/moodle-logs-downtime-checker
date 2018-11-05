#!/usr/bin/env python
import argparse
import csv

def checkForDowntime(time1, time2, maxDowntimeMins):
    (time1H, time1M) = time1.split(':')
    (time2H, time2M) = time2.split(':')
    time1H = int(time1H)
    time1M = int(time1M)
    time2H = int(time2H)
    time2M = int(time2M)

    if (time1H > time2H):
        hoursDiff = time1H - time2H
        time1M += (60 * hoursDiff)

    minsDiff = time1M - time2M
    if (minsDiff >= maxDowntimeMins):
        print 'Significant downtime spotted ' + time2 + ' - ' + time1


def main():
    parser = argparse.ArgumentParser('%prog -f <logs csv file> -m <max downtime minutes>')
    parser.add_argument('-f', dest='csv', help='Specify logs csv file')
    parser.add_argument('-m', dest='mins', help='Specify maximum downtime minutes')
    args = parser.parse_args()

    if (args.csv == None or args.mins == None):
		print '[-] You must specify a target csv file and maximum downtime minutes'
		exit(0)

    with open(args.csv) as csvfile:
        reader = csv.DictReader(csvfile)
        index = 0
        times = []
        for row in reader:
            time = row['\xef\xbb\xbfTime'][-5:]
            times.append(time)

        for index, time in enumerate(times):
            try:
                nextTime = times[index + 1]
                checkForDowntime(time, nextTime, int(args.mins))
            except:
                pass

if __name__ == '__main__':
	main()
