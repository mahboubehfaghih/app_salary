from flask import Flask, request, render_template

app = Flask(__name__)
salary = 0
bonus = 0
taxes = 0
total = 0

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        salary = float(request.form.get("salary"))
        bonus = float(request.form.get("bonus"))
        taxes = float(request.form.get("taxes"))
        total = salary+bonus-taxes
        
        
    else:
        total=0
    return render_template("website.html",total=total)
if __name__ == '__main__':
    app.run(port= 5000, debug=True)