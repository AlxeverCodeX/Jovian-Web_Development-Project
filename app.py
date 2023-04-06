from flask import Flask, render_template,jsonify

app = Flask(__name__)


JOBS = [
    {
    'id':1,
    'title': 'Data Analyst',
    'location': 'Nigeria',
    'salary': 'N 350,000'},
    {
    'id':2,
    'title': 'Data Scientist',
    'location': 'Nigeria',
    'salary': 'N 500,000'},
    {
    'id':3,
    'title': 'Front-End Developer',
    'location': 'Remote',
    },
    {
    'id':4,
    'title': 'Back-End Developer',
    'location': 'Canada',
    'salary': '$ 250,000'}
]

@app.route("/")
def hello():
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(debug=True) 