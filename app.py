from flask import Flask
from flask import render_template
import os
app = Flask(__name__,static_folder='build',template_folder='templates')


def sorted_ls(path):
    mtime = lambda f: os.stat(os.path.join(path, f)).st_mtime
    return list(sorted(os.listdir(path), key=mtime,reverse=True))


@app.route("/")
def hello_world():
    return render_template("welcome.html")

# render posts and filename
@app.route("/posts/<filename>")
def posts(filename):
    # replace space with underscore
    filename = filename.replace(" ","_")
    return render_template("posts/" + filename + ".html")

# bloglist 
@app.route("/blog")
def bloglist():
    # get all files in posts folder and sort them by date descending
    posts = sorted_ls("templates/posts")

    # remove .html from file name
    for i in range(len(posts)):
        posts[i] = posts[i].replace(".html","")
        posts[i] = posts[i].replace("_"," ")


    
    return render_template("bloglist.html",posts=posts)

if __name__ == "__main__":
    app.run(debug=True,port=6000)