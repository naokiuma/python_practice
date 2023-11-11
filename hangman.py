def hangman(word):
	wrong_count = 0
	stages = [
				"",
				"_____         ",
				"              ",
				"       |      ",
				"       0      ",
				"      /|\     ",
				"      /\      ",
			]
	word_list = list(word) # 受け取った単語を配列に
	board = ["_"] * len(word) #文字数分かくす
	win = False #勝利か否か
	print("ハングマンへようこそ！")
	# print(board)
	# print(word_list)
	print('--------------')



	while wrong_count < len(stages) - 1: #舞台の数以上に間違えたら終了
		print("\n")
		msg = "1文字を予想してね"
		input_char = input(msg) #ここに入力文字が入る
		if input_char in word_list:
			cind = word_list.index(input_char) #indexを取得
			board[cind] = input_char
			word_list[cind] = '$'#その文字はすでに選ばれたということで隠す
			# print(word_list)
		else:
			wrong_count += 1
		
		print(" ".join(board))
		e = wrong_count + 1
		print('stateg')
		print("\n".join(stages[0:e]))


hangman('おべんとう')