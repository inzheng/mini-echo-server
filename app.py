from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['Get'])
def index():
    return """
    <html>
        <body>
           he <form action = "/print"  method = "post">
                <p>Please Enter your Name</p>
                Name: <input type = "text" name = "user_name">
                <input type = "submit" value = "Send">
            </form>
        </body>
    </html>
    """

@app.route('/print', methods=['POST'])
def print():
    name = request.form.get('user_name')
    html = """ <html><body><p>Your name is """
    html += name
    html += """</p></body></html>"""
    return html

if __name__ == '__main__':
    app.debug = True
    app.run()
