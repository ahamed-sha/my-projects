import requests

print("welcome to my flight club!\nWe find the best flight deals and notify you.")
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email1 = input("what is your email?\n")
email2 = input("Type your email again to confirm\n")

if email1 == email2:
    post_endpoint = "https://api.sheety.co/2424242424/flightDeals/users"
    query = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email1
        }
    }
    response = requests.post(url=post_endpoint, json=query)
    print(response.text)
    print("Successfully registered!")
else:
    print("The two emails doesn't match!, try again")
