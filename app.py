from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# List untuk simpan data absen sementara di memori
data_absensi = []

@app.route('/')
def home():
    return "Sistem H17 Aktif. Akses /generate atau /check"

@app.route('/generate')
def generate():
    return render_template('generate.html')

@app.route('/check')
def check():
    return render_template('check.html')

@app.route('/api/absen', methods=['POST'])
def api_absen():
    nama = request.json.get('nama')
    waktu = datetime.now().strftime("%H:%M:%S")
    if nama:
        data_absensi.append({"nama": nama, "waktu": waktu})
        return jsonify({"status": "ok", "msg": f"{nama} absen jam {waktu}"})
    return jsonify({"status": "error"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')