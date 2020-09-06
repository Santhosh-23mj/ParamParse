#!/usr/bin/python3

import re
import os
import argparse

banner = """
###########################################################
               ParamSpider Output Parser
    Parse the ParamSpider output and make simple files
###########################################################
"""

"""
Function to create seperate files for each param, triggered
with the -s flag
"""
def createFiles(linksDic):
	if(not os.path.isdir('output')):
		os.mkdir('output')
	
	for param in linksDic.keys():
		if(len(linksDic[param]) > 5):
			filename = os.path.join('output',param+'.txt')
			with open(filename, "w") as f:
				for link in linksDic[param]:
					f.write(link)
		else:
			filename = os.path.join('output','lessfreq.txt')
			with open(filename,"a") as f:
				for link in linksDic[param]:
					f.write(link)


"""
Function to print out the stats of the paramater occurence
"""
def printParams(filename):
	with open(filename) as file:
		links    = file.readlines()
		countDic = {}
		urlDic   = {}
		# Getting the params
		for link in links:
			exp = r"\?(.*)="
			mat = re.search(exp, link)	
			if(mat[1] not in countDic.keys()):
				countDic[mat[1]] = 1
				urlDic[mat[1]] = []
				urlDic[mat[1]].append(link)
			else:
				countDic[mat[1]] += 1
				urlDic[mat[1]].append(link)
			# Sorting based on frequency
			countDic = {k: v for k,v in sorted(countDic.items(), key = lambda kv: kv[1], reverse=True)}
		print("---------------------------------------")
		print("       PARAMETER COUNT STATS      ")
		print("---------------------------------------")
		print("{:<20} {:<20}".format("PARAMETER","COUNT"))
		print("{:<20} {:<20}".format("----------","-------"))
		for key, value in countDic.items():
			print("{:<20} {:<20}".format(key, value))
		print("---------------------------------------")
		print("[+] Total unique parameters      :   "+str(len(urlDic.keys())))
	return urlDic

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-f","--filename", help = "Output file of ParamSpider", required = True)
	parser.add_argument("-s","--seperate", help = "Create seperate files for all different params", action = 'store_true')
	args   = parser.parse_args()
	
	print(banner)
	linksDic = printParams(args.filename)
	
	if(args.seperate):
		print("=======================================")
		print("Creating Seperate files...")
		createFiles(linksDic)
		print("Done!")
		print("=======================================")


if(__name__ == "__main__"):
	main()
