import psutil
import csv


file = open("data.txt","w")

for conn in psutil.net_connections(kind = 'tcp'):
	laddr = '"%s@%s"' % conn.laddr
	pid = "%s" % conn.pid
	status = '"%s"' % conn.status
	if conn.raddr:
		raddr = '"%s@%s"' % (conn.raddr)	
		data1 = "%s,%s,%s,%s\n" % (pid,laddr,raddr,status)
		file.write(data1)

file.close()
file = open('data.txt','r')
data = csv.reader(file,delimiter=",")

result = sorted(data, key = lambda x : int(x[0]))
print "'PID',","'LADDR',","'RADDR',","'STATUS'"

for i in result:
	print str(i).replace('[','').replace(']','')