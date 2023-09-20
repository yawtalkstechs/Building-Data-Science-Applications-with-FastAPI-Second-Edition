from pydantic import BaseModel, EmailStr, ValidationError, model_validator


class UserRegistration(BaseModel):
    email: EmailStr
    password: str
    password_confirmation: str

    @model_validator(mode='after')
    def passwords_match(self):
        password = self.password
        password_confirmation = self.password_confirmation
        if password is not None and password_confirmation is not None and password != password_confirmation:
            raise ValueError('passwords do not match')
        return self


# Passwords not matching
try:
    UserRegistration(
        email="jdoe@example.com", password="aa", password_confirmation="bb"
    )
except ValidationError as e:
    print(str(e))

# Valid
user_registration = UserRegistration(
    email="jdoe@example.com", password="aa", password_confirmation="aa"
)
# email='jdoe@example.com' password='aa' password_confirmation='aa'
print(user_registration)
