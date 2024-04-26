def process_form_data(data):
    try:
        # Simulating dynamic conditions for form validation
        if 'email' in data:
            if '@' not in data['email']:
                raise ValueError("Invalid email format")

        if 'age' in data:
            age = int(data['age'])
            if age < 18:
                raise ValueError("Age must be 18 or above")

        # Process the form data if all conditions are met
        print("Form data processed successfully!")

    except KeyError as e:
        print(f"Missing required field: {e}")

    except ValueError as e:
        print(f"Validation error: {e}")


# Simulated form data with changing conditions
form_data1 = {'email': 'example.com', 'age': '25'}
form_data2 = {'name': 'John Doe', 'age': '15'}

# Process form data with exception handling
process_form_data(form_data1)
process_form_data(form_data2)


class Form:
    data = {}

    def __init__(self, name, age, experience, email):
        self.name = name
        self.age = age
        self.experience = experience
        self.email = email

    def details(self):
        self.data["name"] = self.name
        self.data["age"] = self.age
        self.data["experience"] = self.experience
        self.data["email"] = self.email

        try:
            if not isinstance(self.name, str):
                raise ValueError("Enter the correct name")
            elif not isinstance(self.age, int):
                raise ValueError("Enter the integer value of age")
            elif not isinstance(self.experience, int):
                raise ValueError("Enter the experience in integer value")
            elif '@' not in self.email:
                raise ValueError("Invalid Email")
        except ValueError as e:
            print(e)

        print(self.data)


c = Form("Siya", 24, 1, 'example@example.com')
print(c.details())
c1 = Form("Siya", 'er', 1,'exampleexample.com')
print(c1.details())

