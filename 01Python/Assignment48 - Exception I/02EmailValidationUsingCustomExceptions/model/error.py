class DotException(Exception):
    pass


class AtTheRateException(Exception):
    pass


class DomainException(Exception):
    pass


def validate_email(email):
    if email.count("@") != 1:
        raise AtTheRateException("Invalid @ Usage")
    at_pos = email.index("@")

    if "." not in email[at_pos + 1 :]:
        raise DotException("Invalid Dot Usage")

    print(email.split("."))
    print(email.split(".")[-1])

    domain = email.split(".")[-1]

    if domain not in ["com", "in", "net", "biz"]:
        raise DomainException("Invalid Domain Usage")
