Log file used:- 

Nov  9 10:50:56 ubuntu dhclient[4406]: DHCPDISCOVER on ens33 to 255.255.255.255 port 67 interval 3 (xid=0x877d0360)
Nov  9 10:50:58 ubuntu avahi-daemon[871]: Joining mDNS multicast group on interface ens33.IPv6 with address fe80::e62d:95d1:f83c:fbfe.
Nov  9 10:50:58 ubuntu avahi-daemon[871]: New relevant interface ens33.IPv6 for mDNS.
Nov  9 10:50:58 ubuntu avahi-daemon[871]: Registering new address record for fe80::e62d:95d1:f83c:fbfe on ens33.*.
Nov  9 10:50:59 ubuntu dhclient[4406]: DHCPDISCOVER on ens33 to 255.255.255.255 port 67 interval 7 (xid=0x877d0360)
Nov  9 10:51:00 ubuntu whoopsie[1344]: [10:51:00] Cannot reach: https://daisy.ubuntu.com
Nov  9 10:51:00 ubuntu whoopsie[1344]: [10:51:00] Cannot reach: https://daisy.ubuntu.com
Nov  9 10:51:06 ubuntu dhclient[4406]: DHCPDISCOVER on ens33 to 255.255.255.255 port 67 interval 8 (xid=0x877d0360)
Nov  9 10:51:14 ubuntu dhclient[4406]: DHCPDISCOVER on ens33 to 255.255.255.255 port 67 interval 13 (xid=0x877d0360)
Nov  9 10:51:27 ubuntu dhclient[4406]: DHCPDISCOVER on ens33 to 255.255.255.255 port 67 interval 14 (xid=0x877d0360)
Nov  9 10:51:41 ubuntu dhclient[4406]: DHCPDISCOVER on ens33 to 255.255.255.255 port 67 interval 14 (xid=0x877d0360)
Nov  9 10:51:41 ubuntu NetworkManager[902]: <warn>  [1541789501.2718] dhcp4 (ens33): request timed out
Nov  9 10:51:41 ubuntu NetworkManager[902]: <info>  [1541789501.2719] dhcp4 (ens33): state changed unknown -> timeout
Nov  9 10:51:41 ubuntu NetworkManager[902]: <info>  [1541789501.3053] dhcp4 (ens33): canceled DHCP transaction, DHCP client pid 4406
Nov  9 10:51:41 ubuntu NetworkManager[902]: <info>  [1541789501.3054] dhcp4 (ens33): state changed timeout -> done
Nov  9 10:51:41 ubuntu NetworkManager[902]: <info>  [1541789501.3059] device (ens33): state change: ip-config -> failed (reason 'ip-config-unavailable') [70 120 5]

I am trying to extract the following using the above log file:-
i) Extract the process ID from each line of the log file
ii)	Extract the names of all the processes that generated the log files
iii) Extract the specific port numbers that the process uses (if any)
iv)	Extract only the ‘informational’ logs from the log file.

******Python script#1*******
i) Extract the process ID from each line of the log file

print ("Hello user! Below are the process IDs for the log aggregated:-")

with open(r"C:\Users\aisha\Desktop\pythonLog\log1.txt") as f:
	for line in f:
		num = line[line.find("[")+1 : line.find("]")]
		print(num)

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
OUTPUT
---------

Hello user! Below are the process IDs for the log aggregated:-
4406
871
871
871
4406
1344
1344
4406
4406
4406
4406
902
902
902
902
902

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




******Python script#2*******
ii) Extract the names of all the processes that generated the log files

import re

print('\n')
print ("Hello user! Following types of logs were generated on your device :-")

glist = []
with open(r"C:\Users\aisha\Desktop\pythonLog\log1.txt") as f:
	for line in f:
		match = re.search(r'ubuntu ([a-zA-Z]*-?[a-zA-Z]*)', line)
		if match:
			glist.append(match.group(1))
		else:
			print("Not found") 
			
	
	u = set(glist)
	print(u)

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
OUTPUT
---------

Hello user! Following types of logs were generated on your device :-
{'avahi-daemon', 'NetworkManager', 'whoopsie', 'dhclient'}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




******Python script#3*******
iii) Extract the specific port numbers that the process uses (if any)

import re

with open(r"C:\Users\aisha\Desktop\pythonLog\log1.txt") as f:
	for line in f:
		match = re.search(r'port [0-9]+', line)
		if match: 
			print(match.group())
		else:
			print("port number not found")

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
OUTPUT
---------

port 67
port number not found
port number not found
port number not found
port 67
port number not found
port number not found
port 67
port 67
port 67
port 67
port number not found
port number not found
port number not found
port number not found
port number not found

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



******Python script#4*******
iv) Extract only the ‘informational’ logs from the log file.

print('\n')
print ("Hello user! Here are some of the info logs:-")

with open(r"C:\Users\aisha\Desktop\pythonLog\log1.txt") as f:
	for line in f:
		targets = [line for line in f if '<info>' in line]
		for l in targets:
			print(l)

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
OUTPUT
---------

Hello user! Here are some of the info logs:-
Nov  9 10:51:41 ubuntu NetworkManager[902]: <info>  [1541789501.2719] dhcp4 (ens33): state changed unknown -> timeout

Nov  9 10:51:41 ubuntu NetworkManager[902]: <info>  [1541789501.3053] dhcp4 (ens33): canceled DHCP transaction, DHCP client pid 4406

Nov  9 10:51:41 ubuntu NetworkManager[902]: <info>  [1541789501.3054] dhcp4 (ens33): state changed timeout -> done

Nov  9 10:51:41 ubuntu NetworkManager[902]: <info>  [1541789501.3059] device (ens33): state change: ip-config -> failed (reason 'ip-config-unavailable') [70 120 5]

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

