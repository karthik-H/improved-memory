import re


def validate_user_email(email: str) -> bool:
    valid_domain = ["gmail.com", "yahoo.com"]
    # Simple regex for validating an email address
    pattern = r"^[a-zA-Z0-9._%+-]+@@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email) is None:
        return "Invalid email format"

    domain = email.split("@")[-1]

    if domain not in valid_domain:
        return "Invalid email domain"
    else:
        return "Valid email address"
