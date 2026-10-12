from model.error import (
    AtTheRateException,
    DomainException,
    DotException,
    validate_email,
)

email = input("Enter Email : ")

try:
    validate_email(email)
except AtTheRateException as e:
    print(e)
except DotException as e:
    print(e)

except DomainException as e:
    print(e)
else:
    print("Correct Email")
