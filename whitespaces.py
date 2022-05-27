#whitespaces
#stripping over whitespaces
#whitespaces are whitespaces, newlines, tabs
greet="hello bob"
print(greet)
greet="\nhello bob" #newline
print(greet)
greet="  hello bob" #bunchofspaces
print(greet)
greet="  hello bob  "
print(greet)
greet.strip()
#>> will remove spaces from both sides
greet.lstrip()
#>>will remove spaces from left
greet.rstrip()
#>>remove spaces from right