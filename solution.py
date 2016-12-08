from flask import Flask, render_template, request, url_for
app = Flask(__name__, )
import rectification
from PIL import Image

@app.route('/rectification', methods=["GET", "POST"])
def web_rectificate():
    if request.method == "POST":
        coords = request.form['general']

        im = request.files['pic']
        ext = im.filename[im.filename.find('.'):]
        filname = "uploads/" + str(random.randint(0, 100000000))
        init_im_addr = url_for("static", filename=filname + ext)
        im.save('static/' + filname + ext)
        im = Image.open('static/' + filname + ext)
        
        coords = coords.split()
        r = []
        for el in range(len(coords)):
            if el % 2 == 0:
                z = []
                coords[el] = int(coords[el])
                z.append(coords[el])
            elif coords[el][-1] == ';':
                z.append(int(coords[el][:-1]))
                r.append(z)
#
        coords = r

        print(coords)

        try:
            new_im_addr = url_for("static", filename=rectification.rectificate(im, coords))
        except rectification.WrongCoordinatesException:
            #if we get wrong coordinates exception we show the same image
            new_im_addr = url_for("static", filename="exception.png")

        return render_template("index.html", im=init_im_addr, new_im=new_im_addr)
    else:
        return render_template("index.html")


if __name__ == '__main__':
   app.run(debug=True)
