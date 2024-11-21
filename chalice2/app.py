from chalice import Chalice
import boto3
app = Chalice(app_name='chalice2')
instance_id='id-1234567890'
ecs=boto3.client('ec2')

@app.route('/')
def index():
    return {'hello': 'world'}

@app.schedule('cron (0 0 * * *)')
def daily_task():
    print("running daily task at midnight")
    response=ec2.start_instances(instance_id)
# The view function above will return {"helo": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
