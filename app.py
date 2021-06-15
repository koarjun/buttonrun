from flask import Flask, render_template
from flask_restful import Api
from api_endpoints.run_job import RunJobApi

app = Flask(__name__)
api = Api(app)

api.add_resource(RunJobApi, '/run_job', '/run_job/<job_name>')

@app.route('/')
def home():
    print('Redirecting to home page')
    return render_template("/index.html")