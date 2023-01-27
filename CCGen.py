import json
import argparse
import requests

headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "fake-valid-cc-data-generator.p.rapidapi.com"
}

def generate_cc(cc_type: str, count: int) -> None:
    url = "https://fake-valid-cc-data-generator.p.rapidapi.com/request/"
    querystring = {"visa_type": cc_type}

    for i in range(count):
        response = requests.get(url, headers=headers, params=querystring)
        response_data = json.loads(response.text)
        if 'message' in response_data and response_data['message'] == "You have exceeded the DAILY quota for Requests on your current plan, BASIC. Upgrade your plan at https://rapidapi.com/ApiKeyHunter/api/fake-valid-cc-data-generator":
            print("Error: you have exceeded your daily quota. Upgrade your plan at https://rapidapi.com/ApiKeyHunter/api/fake-valid-cc-data-generator")
            return
        print(f"Type: {response_data['type']}")
        print(f"Firstname: {response_data['firstname']}")
        print(f"Lastname: {response_data['lastname']}")
        print(f"CC Information: {response_data['cc']}|{response_data['valid_date']}|{response_data['cvc']}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate fake credit card data')
    parser.add_argument('--cc_type', help='Type of credit card (visa, mastercard, etc.)', required=True)
    parser.add_argument('-c', '--count', help='Number of credit card to generate', type=int, default=1)
    args = parser.parse_args()

    if args.cc_type:
        generate_cc(args.cc_type, args.count)
    else:
        parser.print_help()
