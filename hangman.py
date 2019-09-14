import random
wordList=['test','adventure','classroom','selection','commercial']
def selectedWord():
	return random.choice(wordList)

def updateWord(inputValue,blankDashes,var):
	result = ''
	for i in range(len(var)):
		if var[i]==inputValue:
			result = result + inputValue
		else:
			result = result + blankDashes[i]

	return result

def guessLetter():
	var = selectedWord()
	print var
	wordLength = len(var)
	print(wordLength)
	blankDashes = '_'*wordLength
	print blankDashes
	i = 1
	invalidOptionCount = 7
	while invalidOptionCount <= 7:
		if '_' not in blankDashes:
			print "You Won"
			break
		print invalidOptionCount
		if invalidOptionCount == 0:
			print 'You Lost'
			break
		userInput = raw_input('Guess the letter ')
		if len(userInput) > 1:
			print 'input exactly one character'
		else:
			if userInput in var and userInput not in blankDashes:
				blankDashes = updateWord(userInput,blankDashes,var)
				print blankDashes
			elif userInput in blankDashes:
				print "You have already entered this character"
				print blankDashes
			else:
				invalidOptionCount -= 1
				print 'This character does not exist in the secret word'	
		i +=1


guessLetter()	
