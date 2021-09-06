from flask import Flask,render_template
from flask.globals import request
import bs_lgc

app = Flask(__name__)


@app.route('/search/text',methods=['POST'])
def search_text():
    request_data = request.get_json()
    coordinate_list = eval(request_data['body']['position'])
    x0,y0,x2,y2 = coordinate_list[0],coordinate_list[1],coordinate_list[2],coordinate_list[3]
    fname = request_data['body']['file_name']
    result = bs_lgc.get_text(x0,y0,x2,y2,fname)
    response = {'text':result}
    return response

if __name__ == "__main_":
    app.run(host='localhost',debug=True,port=5000)
