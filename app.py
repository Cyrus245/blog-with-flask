import requests
from flask import Flask, render_template, request, redirect
import smtplib
from dotenv import dotenv_values

config = {**dotenv_values("venv/.env")}

app = Flask(__name__)


@app.route("/post/<int:p_id>")
def get_post(p_id):
    blog_posts = requests.get("https://api.npoint.io/65af5396f563b009b3dd").json()
    return render_template("post.html", post_id=p_id, all_posts=blog_posts)


@app.get("/")
def get_home():  # put application's code here
    blog_data = requests.get("https://api.npoint.io/65af5396f563b009b3dd").json()
    print(blog_data)
    return render_template("index.html", data=blog_data)


@app.get("/about")
def get_about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact_handler():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(
                user=config["sender_email"], password=config["sender_pass"]
            )
            connection.sendmail(
                from_addr=config["sender_email"],
                to_addrs=config["receiver_email"],
                msg=f"Subject:Blog contact Form\n\nName:{name}\nEmail:{email}\nPhone:{phone}\nMessage:{message}",
            )

        # sending msg in template files
        return render_template("contact.html", msg=True)

    if request.method == "GET":
        return render_template("contact.html", msg=False)


if __name__ == "__main__":
    app.run(debug=True)
