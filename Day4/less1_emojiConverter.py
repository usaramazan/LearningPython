message='Good morning sunshine !'
words=message.split(' ')#list seklinde return ediyor
print(words)

emoji={
    ':)':'😀',
    '!':'☀️'
}
output=''
for each in words:
     output+=emoji.get(each,each)+' '

print(output)