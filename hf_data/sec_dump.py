import urllib.request
import time

INDEX_BASE = "https://www.sec.gov/Archives/edgar/full-index/%s/%s/master.idx"
OUTPATH = "data/sec_root/%s_%s.txt"

def main():
	##set subdirectory lists
	years = [str(n) for n in range(1994, 2018)]
	qtrs = ['QTR1', 'QTR2', 'QTR3', 'QTR4']

	# run through every permutation and request
	# master.idx file, store in sec_master/

	for y in years:
		for q in qtrs:
			time.sleep(10)
			print(INDEX_BASE % (y,q))
			urllib.request.urlretrieve(INDEX_BASE % (y,q), OUTPATH % (y,q))

if __name__ in "__main__":
	main()
