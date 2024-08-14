from flask import Flask, render_template, jsonify, request
import time

app = Flask(__name__)

channels = {
    'food': [
    {
        'name': 'Samincgs',
        'msg': 'I love chocolate!',
        'time': 0,
    },
    {
        'name': 'Denise',
        'msg': 'Me too!',
        'time': 1,
    },
    {
        'name': 'Denji',
        'msg': 'Ugh',
        'time': 2,
    },
  ],
     'games': [
    {
        'name': 'Zilly',
        'msg': 'I love vaegrant',
        'time': 0,
    },
    {
        'name': 'Brush',
        'msg': 'It needs work.',
        'time': 1,
    },
    {
        'name': 'potato',
        'msg': 'Its amazing!',
        'time': 2,
    },
  ],
    
}

def clean(string):
    return string.replace('<', '').replace('>', '')

# option 1
# f = open('messaging.html', 'r')
# messaging_layout = f.read()
# f.close()
# return messaging_layout

@app.route('/')
def home():
    output = 'Welcome to my home. We appear to be lacking in <i>furniture</i>.<br><br>Channels:<br>'
    for channel in channels:
        output += f'<a href="/channel/{channel}">#{channel}</a><br>'
    return output

@app.route('/channel/<channel_id>')
def channel(channel_id):
    #option 2
    return render_template('messaging.html')
    # output = '<a href="/">Home Page</a><br><br>'
    # for message in channels[channel_id]:
    #     output += message + '<br>'
    # return output

@app.route('/api/channels')
def api_channels():
    return jsonify(list(channels))

@app.route('/api/channel/<channel_id>')
def api_channel(channel_id):
    return jsonify(channels[channel_id])

@app.route('/api/send_message', methods=['POST'])
def api_send_message():
    sent_message = request.json()
    
    channel = sent_message['channel']
    
    message_data = {
        'msg': clean(sent_message['msg']),
        'name': clean(sent_message['name']),
        'time': time.time(),
    }
    
    channels['channel'].append(message_data)
    
    return jsonify({'status': 'sucess'})

if __name__ == '__main__':
    app.run(port=3000, debug=True)
    