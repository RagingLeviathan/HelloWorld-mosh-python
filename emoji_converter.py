message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😄",
    ":(": "☹️",
    "o3o": "😗",
    ":'(": "😢",
    ":P": "😛"
}
output = ''
for word in words:
    output += emojis.get(word, word) + " "
print(output)