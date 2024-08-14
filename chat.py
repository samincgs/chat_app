from flask import Flask

app = Flask(__name__)

channels = {'c1': ['hey!', 'hello!'], 'c2': ['eeeee', 'ooooo', 'ahhhhhh']}

f = open('messaging.html', 'r')
messaging_layout = f.read()
f.close()

@app.route('/')
def home():
    output = 'Welcome to my home. We appear to be lacking in <i>furniture</i>.<br><br>Channels:<br>'
    for channel in channels:
        output += f'<a href="/channel/{channel}">#{channel}</a><br>'
    return output

@app.route('/channel/<channel_id>')
def channel(channel_id):
    return messaging_layout
    # output = '<a href="/">Home Page</a><br><br>'
    # for message in channels[channel_id]:
    #     output += message + '<br>'
    # return output

if __name__ == '__main__':
    app.run(port=3000, debug=True)
    