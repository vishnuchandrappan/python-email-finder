from template import mailArray
from validate_email import validate_email


def createEmailList(first_name, last_name, domain):
    fi = first_name[0]
    li = last_name[0]

    combinations = []

    for emailId in mailArray:
        temp = [emailId]
        temp[0] = temp[0].replace("{{fn}}", first_name)
        temp[0] = temp[0].replace("{{ln}}", last_name)
        temp[0] = temp[0].replace("{{domain}}", domain)
        temp[0] = temp[0].replace("{{fi}}", fi)
        temp[0] = temp[0].replace("{{li}}", li)

        print(f"Email => {temp[0]}")

        isValid = validate_email(
            email_address=temp[0], check_regex=True, check_mx=True)

        print(f"Validity -> {isValid}")

        if(isValid):
            combinations.append(temp[0])
        else:
            combinations.append("xxx")

    return combinations


def emailFinder(data):
    if data["first_name"] and data["last_name"] and data["domain"]:
        if(len(data["first_name"]) != 0 and len(data["last_name"]) != 0):
            return createEmailList(data["first_name"], data["last_name"], data["domain"])


def show(first_name, last_name, domain):
    data = {
        "first_name": first_name,
        "last_name": last_name,
        "domain": domain
    }
    response = emailFinder(data)
    return response


print(show("Anand", "s", "logidots.com"))
