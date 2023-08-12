from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("flask_key")

# Configure Flask-Mail
app.config['MAIL_SERVER'] = os.getenv("mail_server")  # Replace with your SMTP server
app.config['MAIL_PORT'] = os.getenv("mail_port")  # Replace with the appropriate port
app.config['MAIL_USERNAME'] = os.getenv("mail_username")  # Replace with your email
app.config['MAIL_PASSWORD'] = os.getenv("mail_password")  # Replace with your email password
app.config['MAIL_DEFAULT_SENDER'] = os.getenv("mail_username")  # Replace with your email
app.config['MAIL_USE_TLS'] = False  # TLS is not required
app.config['MAIL_USE_SSL'] = True   # SSL is required

mail = Mail(app)

# Route to handle form submission


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact")
def contact():
    """Contact page."""
    return render_template("contact.html")


# Route to handle form submission
@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        phone = request.form.get('phone')
        email = request.form.get('email')
        message = request.form.get('message')

        recipient = os.getenv("mail_username")

        # Create and send the email
        msg = Message('New Contact Form Submission',
                      recipients=[recipient])
        msg.body = f"Name: {name}\nSurname: {surname}\nPhone: {phone}\nEmail: {email}\nMessage: {message}"

        try:
            mail.send(msg)
            print("Worked")
            return "Email sent successfully!"
        except Exception as e:
            print("Didnt work")
            print(f"Error sending email: {str(e)}")
            return f"Error sending email: {str(e)}"



if __name__ == "__main__":
    app.run(debug=False)

