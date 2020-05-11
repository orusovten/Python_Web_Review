from flask import Flask, request, render_template
from processing import do_operation, find_errors_in_text, find_errors_in_operation


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        text = request.form.get("text")
        operation = request.form.get("operation")
        cipher = request.form.get("cipher")
        key = request.form.get("key")
        errors += find_errors_in_text(text)
        else:
            errors += find_errors_in_operation(operation, cipher, key)
        if errors == "":
            result = do_operation(text, operation, cipher, key)
            return render_template("result.html", result=result)
    return render_template("home.html", errors=errors)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
