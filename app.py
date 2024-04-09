from flask import Flask, jsonify, request, render_template
import qrcode
from models.user import User
from pydantic import ValidationError
from database.database import add_to_db
from io import BytesIO


app = Flask(__name__)


@app.route("/")
def hello():
  return render_template("index.html")

@app.route("/form")
def form():
  return render_template("form.html")

def genetateqrcode(data):
  qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
  )
  qr.add_data(data)
  qr.make(fit=True)
  img = qr.make_image(fill_color="purple", back_color="white")
  img_byte_array = BytesIO()
  type(img)
  img.save(img_byte_array)
  return img_byte_array.getvalue()

@app.route("/qrcode", methods=["POST"])
def generateqrcode():
  if request.method == "POST":
    try:
      data = request.get_json()
      user = User(**data)
      qrcode = genetateqrcode(user)
      add_to_db(qrcode, data)

    except ValidationError as e:
      return jsonify({"error": str(e)}), 400
    return jsonify({"success": "qrcode generated successfully"})


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
