import cmd


class HBNBCommand(cmd.Cmd):
	prompt = '(hbnb)'

	def do_quit(self, arg):
		"""Quit comand to exit the program"""
		return True
	
	def do_eof(self, arg):
		"""EOF command to exit the program"""
		return True

	def precmd(self, line):
		line = line.lower()
		return line
if __name__ == '__main__':
	HBNBCommand().cmdloop()