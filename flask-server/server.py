
from flask import Flask,jsonify
import datetime

x = datetime.datetime.now()

app = Flask(__name__)

Name="geek"
Age="22"
Date=x
programming="python"
@app.route('/data')
def get_time():

	return jsonify({
		Name,Age,Date,programming
    })

if __name__ == '__main__':
	app.run(debug=True)
