from flask import Flask, request
app = Flask(__name__)
@app.route('/')
def index():
    return "Welcome to Birthstone Finder"
birthstone_dict = {"January":"Garnet","February":"Amethyst","March":"Aquamarine","April":"White Topaz","May":"Green Onyx","June":"Moonstone","July":"Ruby","August":"Peridot","September":"Sapphire","October":"Opal","November":"Citrine","December":"Blue Topaz"}

@app.route('/birthstone')
def birthstone():
    name = str(request.args.get('name'))
    month = str(request.args.get('month'))
    month_mod = month.capitalize()
    if month_mod not in birthstone_dict:
        return("Please spell the month correctly {},you wrote {}").format(name,month)
    return('Hi {}, Your birthstone is {}').format(name,birthstone_dict[month_mod])


app.run(host='0.0.0.0', port=82)

