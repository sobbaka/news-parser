from flask import Flask, request, render_template
from google_parser import parseNews
from google_export import export_to_Google
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        phrase = request.form['phrase']
        data = parseNews(phrase)
        link = export_to_Google(data)
        return render_template('success.html', link=link)




    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
