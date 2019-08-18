from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def route_index():
    with open("data.csv", "r") as myfile:
        data = [line.strip().split(";") for line in myfile]

    return render_template('index.html', data=data)


@app.route('/story', methods=['GET', 'POST'])
def route_add():
    if request.method == 'POST':
        with open(r'data.csv', 'a') as myfile:
            vals = request.form.values()
            vals = (';').join(vals)
            myfile.write(vals)
            myfile.write("\n")

            #writer = csv.writer(myfile)
            #vals = request.form.values()
            #writer.writerow(vals)

            return redirect('/')

    return render_template('story.html')


if __name__ == "__main__":
    app.run(
        debug=True, # Allow verbose error reports
        port=5000 # Set custom port
    )
