from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        api_key = 'd133cb4179ecf979e2a4266e653c9c01'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = {'error': 'City not found!'}
    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
