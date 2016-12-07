from flask import Flask, render_template, request
app = Flask(__name__, )
import rectification
from PIL import Image

@app.route('/', methods=["GET", "POST"])
def web_rectificate():
    if request.method == "POST":
        print(request.form)
        coords = request.form['general']
        im = request.files['pic']
        ext = im.filename[im.filename.find('.'):]
        im.save('uploads/file' + ext)
        im = Image.open('uploads/file' + ext)
        coords = coords.split()
        r = []
        for el in range(len(coords)):
            if el % 2 == 0:
                z = []
                z.append(int(coords[el][0]))
            else:
                z.append(int(coords[el][0]))
                r.append(z)
        coords = r

        return render_template("index.html", new_im="results/"+rectification.rectificate(im, coords))
    else:
        return render_template("index.html", new_im="results/new.png")


if __name__ == '__main__':
   app.run(debug=True)