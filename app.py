from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for flash messages

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Determine whether the request is JSON or form data
        if request.is_json:
            # Extract data from JSON payload
            username = request.json.get("email")
            password = request.json.get("password")
        else:
            # Extract data from form submission
            username = request.form.get("email")
            password = request.form.get("password")

        # Basic login check (replace with your actual authentication logic)
        if username == "admin@admin.com" and password == "password":  # Example credentials
            flash("Login Successful!", "success")
            # Respond differently based on request type
            if request.is_json:
                # JSON request: respond with JSON success message and redirect URL
                return jsonify({"success": True, "redirect_url": ("https://hcw-at-home.com/hcw-app")})
            else:
                # Form request: redirect directly to dashboard
                return redirect(("https://hcw-at-home.com/hcw-app"))
        else:
            # Login failed, send appropriate response
            if request.is_json:
                # JSON request: send JSON error message
                return jsonify({"success": False, "error": "Invalid Username or Password"}), 401
            else:
                # Form request: flash error message and redirect back to login page
                flash("Invalid Username or Password", "error")
                return redirect(url_for("login"))

    # For GET requests, render the login page
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return "<h1>Welcome to the Dashboard!</h1>"

if __name__ == "__main__":
    app.run(debug=True, port=5050)
