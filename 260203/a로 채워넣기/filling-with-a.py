text = input()
new_text = list(text)

new_text[1]='a'
new_text[-2]='a'

print(*new_text, sep="")