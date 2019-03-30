from flask import Flask, request, session, flash, redirect, url_for
from flask import render_template

from load_data import load_data

app = Flask(__name__)

# the welcome page
@app.route('/index')
def index():
    name = "hahafei"
    return render_template('hello.html', name=name)

#the page shows temperature curve and humidity curve
# @app.route('/')
@app.route('/DHT')
def DHT():
    data_tem = load_data('temperature')
    data_hum = load_data('humdity')
    data_buz = load_data('buzzer')
    time_t = data_tem[1]
    print(time_t)
    temperature = data_tem[0]
    humdity = data_hum[0]
    if (data_buz[0][0] == 1):
        status = 1
    else:
        status = 0
    # print(status)
    return render_template('temperature.html', time=time_t, temperature=temperature, humdity=humdity, state=status)


@app.route('/light')
def light():
    data_light = load_data('light')
    data_roration = load_data('rotation')
    data_led = load_data('led')
    time_t = data_light[1]
    light = data_light[0]
    rotation = data_roration[0]
    led = data_led[0]
    return render_template('light.html', light=light, rotation=rotation, led=led, time=time_t)

@app.route('/sender/light')
def sender():
    value = request.args.get('value', '')
    w_result = open("database/light.txt", "a")
    w_result.write(str(value) + "\n")
    w_result.close()
    return str(value)

@app.route('/')
@app.route('/test')
def test():
    data_light = load_data('light')
    time_t =  data_light[1]
    light = data_light[0]
    return render_template('light.html', light=light, time=time_t)



if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=8100, ssl_context=('../server.crt', '../server.key'))