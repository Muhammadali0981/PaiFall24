# Name: Muhammad Ali
# Date: 1/9/24
# Desc: message builder


def build_message(**info):
    message_parts = []

    for key, value in info.items():
        message_parts.append(f"{key}: {value}")

    message = ', '.join(message_parts)

    return message


message = build_message(name="Ali", age=19, city="Karachi", occupation="teacher")
print(message)