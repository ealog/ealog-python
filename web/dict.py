lst = input('Phone: ')

dic = {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four"
}

for key in lst:
    print(dic[key])


def greet_user(first_name,last_name):
    print(f'Hi, {first_name} {last_name}')
    print('Welcome aboard!')


greet_user("liu","yang")


class Point():
    def move(self):
        pass