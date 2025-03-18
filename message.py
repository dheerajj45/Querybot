from flask import Flask, request, jsonify, render_template
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


def get_response(choice, user_name):
    """Returns chatbot responses based on user choice."""
    responses = {
        1: f"Address Update Response, {user_name}: Update your address in TalentKonnect. Post updating, you'll receive an auto-generated email. Share that email with the transport team along with latitude & longitude.",
        2: f"No-Show Policy, {user_name}: If you encounter 3 no-shows in a 30-day cycle, your profile will be suspended. Approval from Business COO is required for reactivation.",
        3: f"Profile Suspension, {user_name}: Profile suspension occurs due to 3 no-shows within 30 days. To reactivate, seek approval from your Business COO.",
        4: f"Transport Charges, {user_name}: Charges are deducted after cab usage. Example: If you use the cab in January, charges will be deducted in February's payroll.",
        5: f"Cut-off Time to Book/Cancel Cab, {user_name}: Book or cancel login cabs by 17:00hrs the day prior.",
        6: f"Other Queries, {user_name}: Please reach out to the transport team at xyz.com.",
        7: f"Thank you for reaching out, {user_name}. Have a great day!"
    }
    return responses.get(choice, f"Invalid choice, {user_name}. Please select a number between 1-7.")


@app.route("/chatbot", methods=["POST"])
def chatbot():
    """Handles chatbot interactions via API."""
    data = request.get_json()

    user_name = data.get("user_name", "User")
    choice = data.get("choice")

    if not isinstance(choice, int) or choice < 1 or choice > 7:
        return jsonify({"response": f"Invalid choice, {user_name}. Please select a number between 1-7."})

    return jsonify({"response": get_response(choice, user_name)})


if __name__ == "__main__":
    app.run(debug=True)
