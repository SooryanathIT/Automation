#!/usr/bin/env python3

import psutil , shutil

def check_CPU_Util(wait_interval):
	
	res = psutil.cpu_percent(wait_interval)
	
	print(res)

def check_Disk_Util(disk) :
	
	Res = shutil.disk_usage(disk)

	print("Total -> {total} GB | Free -> {free} GB | Used -> {used} GB".format(total = Res.total / 10**9 , free = Res.free/10**9 ,used = Res.used/10**9))



if __name__ == '__main__':

	rounds = 6

	while rounds :

		check_Disk_Util(disk = '/')

		check_CPU_Util(wait_interval = 1)

		rounds-=1

