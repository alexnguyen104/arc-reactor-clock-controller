from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__, template_folder='template')

@app.route('/', methods=['GET'])
def home():
   return render_template('index.html')

@app.route('/changeColor', methods=['GET', 'POST'])
def changecolor():
   r = str(request.args.get('r'))
   g = str(request.args.get('g'))
   b = str(request.args.get('b'))

   if r=="None" or g == "None" or b == "None":
      return "error in color"
   
   color = {
      "r": r,
      "g": g,
      "b": b
   }

   with open("data.json", "r+") as file:
      data = json.load(file)
      data["color"] = color

      file.seek(0)  # rewind
      json.dump(data, file)
      file.truncate()

   return "color changed to " + '('  + r + ',' + g + ','  + b + ')'

@app.route('/changeBrightness', methods=['GET'])
def changeBrightness():
   brightness = str(request.args.get('b'))
   if brightness == 'None': return "error in brightness"

   with open("data.json", "r+") as file:
      data = json.load(file)
      data["brightness"] = brightness

      file.seek(0)  # rewind
      json.dump(data, file)
      file.truncate()

   return "brightness changed to " + brightness

@app.route('/changePower', methods=['GET'])
def changePower():
   power = str(request.args.get('p'))
   if power == 'None': return "error in power"

   with open("data.json", "r+") as file:
      data = json.load(file)
      data["power"] = power

      file.seek(0)  # rewind
      json.dump(data, file)
      file.truncate()

   return "power changed to " + power

@app.route('/checkPower', methods=['GET'])
def checkPower():
   with open("data.json", "r") as file:
      data = json.load(file)   
      return {'power': data["power"]}
   
@app.route('/checkColor', methods=['GET'])
def checkColor():
   with open("data.json", "r") as file:
      data = json.load(file)   
      return {'color': data["color"]}

@app.route('/checkBrightness', methods=['GET'])
def checkBrightness():
   with open("data.json", "r") as file:
      data = json.load(file)   
      return {'brightness': data["brightness"]}

@app.route('/data', methods=['GET'])
def color():
   with open("data.json") as file:
      data = json.load(file)
      return jsonify(data), 200

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0', port=5432)