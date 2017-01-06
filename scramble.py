from itertools import permutations
import subprocess

#Find all permutation of the given words in the file
def unscramble(files):
	puzzle = open(files, 'r')

	#Get each word in the file
	words = {}
	for word in puzzle:

		#Get each permutation of the word
		perm = [''.join(w) for w in permutations(word)]
		words[word] = set(perm)
	return words
		
#Solve puzzle by finding the correct word in dictionary
def sovleScramble(words, key = 'e6982be6-806d-4781-8390-896ff4406dfb'):
	solved = {}
	for word in words:
		for perm in words[word]:
			#Checks the Dictionary API
			proc = subprocess.Popen("php dictionary.php " + perm + " " + key, shell=True, stdout=subprocess.PIPE)
			script_response = proc.stdout.read()

			#If found in dictionary add to list
			if script_response == "True":
				solved[word] = perm
				break
	return solved

def main():
	solved = sovleScramble(unscramble('puzzle.txt'))
	for word in solved:
		print word + ": " + str(solved[word])

if __name__ == "__main__":main()