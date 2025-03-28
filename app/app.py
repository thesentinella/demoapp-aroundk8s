from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Bienvenido al Demo de Kubernetes en Aroundk8s!</h1>
    <img src='/static/aroundk8s.png' alt='Demo Image' style='width:200px;'>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)