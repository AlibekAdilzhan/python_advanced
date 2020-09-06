d = {'aaa' : 'qwerty', 'bbb' : 'wertyu'}

login = input('Please input the login')
password = input('Please input the password')

if login in d.keys():
    if d[login] == password:
        print('passed')
    else:
        print('incorrect password')

else:
    print('incorrect login')