from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def hello():
    return "Hello, World!", 200

@app.route('/api/health-check/')
@metrics.do_not_track()
def healthCheck():
    #some internal checks...
    return "Health check: OK", 200

if __name__ == "__main__":
    app.run(environs, start_response)

