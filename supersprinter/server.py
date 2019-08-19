from flask import Flask, render_template, request, redirect
import data_manager as dm

app = Flask(__name__)


@app.route('/')
def route_index():
    data = dm.get_data_from_csv()

    return render_template('index.html', data=data)


@app.route('/story', methods=['GET', 'POST'])
def route_add():
    if request.method == 'POST':
        with open(r'data.csv', 'a') as myfile:
            vals = list(request.form.values())
            data = dm.get_data_from_csv()
            last_id = data[-1][0]
            vals.insert(0, str(int(last_id)+1))
            vals = (';').join(vals)
            myfile.write(vals)
            myfile.write("\n")

            return redirect('/')

    return render_template('story.html')


if __name__ == "__main__":
    app.run(
        debug=True, # Allow verbose error reports
        port=5000 # Set custom port
    )
