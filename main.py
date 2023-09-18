from flask import Flask, render_template
from scraper import kvalifikanti, performance_entries_list, kvalifikanti_champions, direct_entries_list

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", kn=kvalifikanti, pel=performance_entries_list, kc=kvalifikanti_champions, de=direct_entries_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
