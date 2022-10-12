
from flask import Flask,request
app=Flask(__name__)
@app.route('/models',methods=['POST'])
def helloworld():
    json_received=request.get_json(force=True)
    model_name=json_received['model']
    return f'you are requesting for {model_name}'

if __name__==('__main__'):
    app.run(port=8000,debug=True)