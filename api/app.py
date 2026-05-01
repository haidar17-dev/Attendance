from flask import Flask, render_template, request, jsonify
from pusher import Pusher
import os

app = Flask(__name__)

# Konfigurasi Pusher
# Gunakan Environment Variables di Vercel demi keamanan
pusher_client = Pusher(
  app_id=os.environ.get('2148815'),
  key=os.environ.get('0d2bad661ad218a07eee'),
  secret=os.environ.get('89a575cb1566f4961946'),
  cluster=os.environ.get('ap1'),
  ssl=True
)

@app.route('/generate')
def generate():
    return render_template('generate.html')

@app.route('/check')
def check():
    return render_template('check.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/absen', methods=['POST'])
def api_absen():
    nama = request.json.get('nama')
    if nama:
        # Trigger data ke channel 'h17-channel' dengan event 'absen-hadir'
        pusher_client.trigger('h17-channel', 'absen-hadir', {'nama': nama})
        return jsonify({"status": "success", "msg": f"{nama} tercatat!"})
    return jsonify({"status": "error"}), 400