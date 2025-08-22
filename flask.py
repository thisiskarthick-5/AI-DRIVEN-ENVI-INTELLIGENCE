from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)
API_KEY = "YOUR_OPENWEATHER_API_KEY"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/forecast', methods=['GET'])
def forecast():
    city = request.args.get('city', 'London')
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    data = requests.get(url).json()
    
    rain_forecast = []
    for item in data['list']:
        dt = item['dt_txt']
        rain = item.get('rain', {}).get('3h', 0)
        rain_forecast.append({"time": dt, "rain_mm": rain})
    
    return jsonify({"city": city, "forecast": rain_forecast})

if __name__ == '__main__':
    app.run(debug=True)
