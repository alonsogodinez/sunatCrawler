import os
from flask import Flask,request, jsonify
from ocr import process_image


app = Flask(__name__)

@app.route('/ocr', methods=["POST"])
def ocr():
	
	#supported_formats = ['BMP', 'PNM', 'PNG', 'JFIF', 'JPEG', 'TIFF']
	try:

		url = request.json['image_url']
		output = process_image(url)
		return jsonify({"captcha": output})

		# if any( _format in url for _format in supported_formats):
		# 	output = process_image(url)
		# 	return jsonify({"captcha": output})
		# else:
		# 	return jsonify({"error": "only "+ ' '.join(map(str,supported_formats)) + " files, please"})

	except:
		return jsonify(
			{"error": "Did you mean to send: {'image_url': 'image_url'}"}
		)


@app.errorhandler(500)
def internal_error(error):
	print(str(error)) 


@app.errorhandler(404)
def not_found_error(error):
	print(str(error))


if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)






