from flask import Flask, render_template, request
from gpiozero import LED

led=LED(21)
app = Flask(__name__)



@app.route('/led-control',methods=['POST'])
def led_control():
 data = request.get_json()
 led_state = data.get('ledState')
 if led_state == 'on':
  led.on()
 elif led_state == 'off':
  led.off()
 else:
  print("unknown")
 return "0"

@app.route('/')
def index():
 return render_template('index.html')


if __name__ == '__main__':
 app.run(host="0.0.0.0")
