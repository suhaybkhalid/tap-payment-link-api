from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route("/generate-payment", methods=["POST"])
def generate_payment():
    try:
        headers = {
            "Authorization": f"Bearer {os.getenv('TAP_SECRET_KEY')}",
            "Content-Type": "application/json"
        }
        data = {
            "amount": 29.00,
            "currency": "SAR",
            "threeDSecure": True,
            "save_card": False,
            "description": "AI Resume Service",
            "statement_descriptor": "Qadeer Resume",
            "metadata": {
                "client": "website"
            },
            "customer": {
                "first_name": "Client",
                "email": request.json.get("email", "client@email.com")
            },
            "redirect": {
                "url": "https://your-google-form2-link.com"
            },
            "source": {
                "id": "src_all"
            }
        }

        response = requests.post("https://api.tap.company/v2/charges", json=data, headers=headers)
        return jsonify(response.json()), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def index():
    return "Tap Payment API is running", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

