from flask import Flask, render_template, request,redirect,url_for
from flask_bootstrap import Bootstrap5
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
from flask_wtf import FlaskForm,CSRFProtect
from wtforms import FileField,SubmitField
from wtforms.validators import DataRequired

hex_colors = []
app = Flask(__name__)
Bootstrap5(app)

app.config["SECRET_KEY"] = "jhskdjfhidsfhdk"
csrf = CSRFProtect(app)

def extract_colors(image_path, num_colors=10):
    image = np.array(Image.open(image_path))
    pixels = image.reshape(-1, 3)

    print(pixels)

    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)

    colors = kmeans.cluster_centers_
    return colors.astype(int)

class UploadForm(FlaskForm):
    file=FileField("Upload Your File",validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route('/', methods=['GET', 'POST'])
def home():
    global hex_colors
    upload = UploadForm()
    if request.method == 'POST':
        # Handle file upload
        file = request.files['file']
        image_path = 'uploads/' + file.filename
        file.save(image_path)

        # Extract colors from uploaded image
        colors = extract_colors(image_path)

        # Convert colors to hexadecimal format
        hex_colors = ['#' + ''.join(f'{c:02x}' for c in color) for color in colors]

        print(hex_colors)
        return redirect(url_for('result'))

    return render_template('user.html',form=upload)

@app.route('/result')
def result():
    global hex_colors
    return render_template('result.html', colors=hex_colors)
if __name__ == '__main__':
    app.run(debug=True)
