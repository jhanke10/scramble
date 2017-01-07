from itertools import permutations
import subprocess
import time

#Find all permutation of the given words in the file
def unscramble(files):
	puzzle = open(files, 'r')

	#Get each word in the file
	words = {}
	for word in puzzle:
		word = word.strip()
		#Get each permutation of the word
		perm = [''.join(w) for w in permutations(word)]
		words[word] = set(perm)
	return words
		
#Solve puzzle by finding the correct word in dictionary
def sovleScramble(words, key = ''):
	solved = {}
	for word in words:
		seen = set()
		for perm in words[word]:
			#Checks the Dictionary API
			if seen == [] or perm[:2] not in seen:
				proc = subprocess.Popen("php dictionary.php " + perm + " " + key, shell=True, stdout=subprocess.PIPE)
				script_response = proc.stdout.read()

				#If found in dictionary add to list
				if script_response == "True":
					solved[word] = perm
					break
				else:
					script_response = script_response.split()
					#Use the list of suggestions to narrow down words that are not possible
					possible = [x for x in script_response if len(x) == len(word)]
					solve = False
					for potential in possible:
						#Suggested word in the permutation then that is the answer
						if potential in words[word]:
							solved[word] = potential
							solve = True
							break

						#Get rid of words starting with that two-letter if none of the suggestions were in permutation
						seen.add(perm[:3])
					if solve:
						break
	return solved

def main():
	start = time.time()
	solved = sovleScramble(unscramble('puzzle.txt'))
	end = time.time()
	for word in solved:
		print word + ": " + str(solved[word])
	print 'Time Elapsed: ' +  str(end - start) + 's'

if __name__ == "__main__":main()