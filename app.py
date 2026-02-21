from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

harcamalar = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        tutar = float(request.form["tutar"])
        kategori = request.form["kategori"]
        aciklama = request.form["aciklama"]

        harcamalar.append({
            "tutar": tutar,
            "kategori": kategori,
            "aciklama": aciklama,
            "tarih": datetime.now().strftime("%d.%m.%Y")
        })

        return redirect("/")

    toplam = sum(h["tutar"] for h in harcamalar)

    return render_template(
        "index.html",
        harcamalar=harcamalar[::-1],
        toplam=toplam
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)