import os


def get_file(filename):
    try:
        return open(os.path.join(os.getcwd(), 'app', 'views', filename)).read()
    except IOError as exc:
        return str(exc)


def parse_user_messages(messages):
    parsed_messages = []
    for msg in messages:
        if msg != '':
            parsed_messages.append(str(msg))
    return parsed_messages


def parse_user(user):
    return {
        'user_name': user['user_name'],
        'rating': user['rating'],
        'rang': user['rang'],
        'avatar': user['avatar'],
        'messages': parse_user_messages(user['messages'])
    }


def parse_users(users):
    return list(map(parse_user, users))
