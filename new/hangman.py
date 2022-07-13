#fast and simple way to code hangman game
answer = input('Type the word: ').lower() #gets the input of word
print('\n'*100) #makes empty space so the other person can not see the answer
guessed=['_' for l in answer if l!=' '] #list comprehension
list_of_wrong_guesses=[]
while guessed.count('_')!=0 and len(list_of_wrong_guesses)<10:
	guess = input('guess a letter: ')[0].lower()# we use [0] to prevent errors if they used too many letters
	if guess in answer:
		for i in range(answer.count(guess)):
			guessed[answer.index(guess)]=guess
			answer=answer.replace(guess,'-',1)
	else:
		list_of_wrong_guesses.append(guess)
	print(''.join(guessed))
	print('You have guessed '+str(len(list_of_wrong_guesses))+' wrong\n those being ('+','.join(list_of_wrong_guesses)+')')
	print('You have '+str(10-len(list_of_wrong_guesses))+' more chances')

