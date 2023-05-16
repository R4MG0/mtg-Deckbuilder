def sanitize(ui):
	if(len(ui) > 40): print("to long"); return True
	# Only really Important are {} and ;
	# the rest is to prevent exploitation
	badstring = "!@#$%^&*()_+={|.<>};:"
	for char in ui:
		if char in badstring:
			print(f"bad character {char}")
			return True
	return False
