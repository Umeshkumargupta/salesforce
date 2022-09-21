
from pickle import TRUE
from shop import app
if __name__ =="__main__":
    app.debug=TRUE
    app.run(host="0.0.0.0")
    