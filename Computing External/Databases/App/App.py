from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
      return "<h1>32fveyhbdcdkuAEWFbvdb</h1>"

if __name__ == '__main__':
      app.run(debug=True)
