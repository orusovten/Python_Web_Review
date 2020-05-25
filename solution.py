import os
from flask import Flask, request, render_template, redirect, make_response, send_from_directory, url_for
from werkzeug.utils import secure_filename
from encode_engine import do_operation, find_errors_in_text, find_errors_in_operation


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'docx'])


app = Flask(__name__)
app.config["DEBUG"] = True
app.config['UPLOAD_FOLDER'] = """./uploads"""


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route("/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


@app.route("/", methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        file = None
        try:
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                with open(app.config['UPLOAD_FOLDER'] + "/" + filename, "r") as text_file:
                    text = text_file.read()
        except Exception:
            text = request.form.get("text")
        operation = request.form.get("operation")
        cipher = request.form.get("cipher")
        key = request.form.get("key")
        errors += find_errors_in_text(text)
        errors += find_errors_in_operation(operation, cipher, key)
        if errors == "":
            result = do_operation(text, operation, cipher, key)
            if file is not None:
                out_filename = "result." + filename.rsplit('.', 1)[1]
                with open(app.config['UPLOAD_FOLDER'] + "/" + out_filename, "w") as out_file:
                    out_file.write(result)
                return redirect(url_for("uploaded_file", filename=out_filename))
            else:
                return render_template("result.html", result=result)
    return render_template("home.html", errors=errors)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
