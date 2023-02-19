message = input("Enter your Words: ")
translate = ''
i = len(message)-1
while i>=0:
    translate = translate + message[i]
    i = i-1
print(translate)
#exit()
# raw_input("Press a key to Exit") 