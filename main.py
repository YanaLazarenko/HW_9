phone_book = {}


def input_error(func):
    def inner_func(*args):
        try:
            return func(*args)
        except IndexError:
            return 'Please enter command, name, phone number'
        except ValueError:
            return 'Pleease enter correct number'
        except KeyError:
            return 'Name is not in phone book'
        except TypeError:
            return 'Unknown comand'
    return inner_func


@input_error
def change_phone(*args):
    for key in phone_book.keys():
        if args[0] == key:
            phone_book[key] = args[1]
            return key, phone_book[key]
    raise KeyError


@input_error
def whose_phone(*args):
    for key, value in phone_book.items():
        if args[0] == key:
            return value
    raise KeyError


@input_error
def add(*args):
    name = args[0]
    phone = args[1]
    if name and phone:
        phone_book[name] = phone
        return f'{name} successfuly added'


def show_all(*args):
    return phone_book


def hello(*args):
    return 'How can I help you?'


def no_comand():
    return 'Please enter your comand'


COMMANDS = {
    'hello': hello,
    'add': add,
    'change': change_phone,
    'phone': whose_phone,
    'show all': show_all,
    'no comands': no_comand,
}

COMMANDS_EXIT = ['exit', 'quit', 'good bye']


def parser(text: str) -> tuple[callable, list]:
    for kwd, comand in COMMANDS.items():
        if text.lower().startswith(kwd):
            args = text[len(kwd):].strip().split(' ')
            return comand, args
    return no_comand, []


def main():
    while True:
        user_input = input('Please enter comand:')
        if not user_input:
            no_comand()
        elif user_input.lower() in COMMANDS_EXIT:
            break
        else:
            comand, args = parser(user_input)
            result = comand(*args)
            print(result)


if __name__ == '__main__':
    main()
