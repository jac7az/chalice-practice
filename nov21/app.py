from chalice import Chalice

app = Chalice(app_name='nov21')

@app.route('/')
def index():
    return {'hello': 'world'}
@app.route('/c')
def hello():
    return {'Howdy':'cat'}
