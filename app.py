from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd
import os
from pokeranalysis import PokerAnalysis
app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for session handling and flashing messages

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_file():
    return render_template('upload.html')

@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']

        # If user does not select file, browser also submits an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Process the CSV file
            analysis = PokerAnalysis(file_path)
            data = analysis.session.player_statistics_table_pandas_df()
            #print(data)
            #data = pd.read_csv(file_path)
            return render_template('table.html', tables=[data.to_html()], titles=data.columns.values)
        else:
            flash('Allowed file type is CSV')
            return redirect(request.url)

    return redirect(url_for('upload_file'))

if __name__ == '__main__':
    app.run(debug=True)