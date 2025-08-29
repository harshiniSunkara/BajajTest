from flask import Flask, request, jsonify
import re
from datetime import datetime
from collections import OrderedDict

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def bfhl():
    try:
        # Replace these with your real details
        full_name = "harshini_sunkara"
        email = "sunharshini@gmail.com"
        roll_number = "22BCE2373"
        dob = "2608004"  # DDMMYYYY
        user_id = f"{full_name.lower()}_{dob}"

        data = request.get_json()
        input_array = data.get("data", [])

        even_numbers = []
        odd_numbers = []
        alphabets = []
        special_characters = []
        total_sum = 0
        concat_letters = ""

        for item in input_array:
            if item.isdigit():
                number = int(item)
                total_sum += number
                if number % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
            elif item.isalpha():
                alphabets.append(item.upper())
                concat_letters += item
            else:
                special_characters.append(item)

        # Alternating caps in reverse
        reversed_concat = concat_letters[::-1]
        formatted_concat = ''
        for i, c in enumerate(reversed_concat):
            formatted_concat += c.upper() if i % 2 == 0 else c.lower()

        response = OrderedDict([
    ("is_success", True),
    ("user_id", user_id),
    ("email", email),
    ("roll_number", roll_number),
    ("odd_numbers", odd_numbers),
    ("even_numbers", even_numbers),
    ("alphabets", alphabets),
    ("special_characters", special_characters),
    ("sum", str(total_sum)),
    ("concat_string", formatted_concat)
])

        return jsonify(response), 200

    except Exception as e:
        return jsonify({
            "is_success": False,
            "message": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
