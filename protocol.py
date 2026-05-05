def handle_message(message: str) -> str:
    parts = message.strip().split()

    if not parts:
        return "ERROR empty message"

    command = parts[0].upper()

    if command == "PING":
        return "PONG"

    if command == "ECHO":
        # TODO: return the text after ECHO
        return " ".join(parts[1:])

    if command == "UPPER":
        # TODO: convert the remaining text to uppercase
        text = " ".join(parts[1:])
        return text.upper()

    if command == "ADD":
        # TODO: add two integers like: ADD 1 2
        if len(parts) != 3:
            return "ERROR invalid arguments"
        try:
            num1 = int(parts[1])
            num2 = int(parts[2])
            return str(num1 + num2)
        except ValueError:
            return "ERROR invalid arguments"

    return "ERROR unknown command"
