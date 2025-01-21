let lastMessages = ''
const messagesElem = document.getElementById('messages')
const messageInput = document.getElementById('message-input')
const channelsElem = document.getElementById('channels')

// function getJSON(url, callback) {
//   const request = new XMLHttpRequest()

//   request.open('GET', url, true)

//   request.onload = () => {
//     if (request.status == 200) {
//       callback(JSON.parse(request.response))
//     }
//   }

//   request.send(null)
// }

async function getJSON(url, callback) {
  try {
    const response = await fetch(url)

    if (!response.ok) {
      console.error(`HTTP Error: ${response.status}`)
      return
    }

    const data = await response.json()
    callback(data)
  } catch (error) {
    console.error('Network Error: ', error)
  }
}

async function postJSON(url, data) {
  try {
    const request = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json;' },
      body: JSON.stringify(data),
    })

    if (!request.ok) {
      console.error('HTTP Error: ' + request.status)
      return
    }
  } catch (error) {
    console.error('Network error: ', error)
  }
}

function getCurrentChannel() {
  let currentChannel = window.location.href.split('/')
  currentChannel = currentChannel[currentChannel.length - 1]
  return currentChannel
}

function updateMessageHTML(messageData) {
  if (JSON.stringify(messageData) != lastMessages) {
    messagesElem.innerHTML = ''

    messageData.forEach((message) => {
      const newMessage = document.createElement('div')
      newMessage.innerHTML =
        '<b class="message-name">' +
        message['name'] +
        ':' +
        '</b>' +
        message['msg']

      newMessage.classList.add('message')
      messagesElem.appendChild(newMessage)
    })

    lastMessages = JSON.stringify(messageData)

    messagesElem.lastChild.scrollIntoView(false)
  }
}

function updateChannelList(channels) {
  const currentChannel = getCurrentChannel()
  channelsElem.innerHTML = ''

  channels.forEach((channel) => {
    const newChannel = document.createElement('a')
    newChannel.text = '#' + channel
    newChannel.href = '/channel/' + channel
    newChannel.classList.add('channel-name')

    if (channel == currentChannel) {
      newChannel.style.textDecoration = 'underline'
    }

    channelsElem.appendChild(newChannel)
  })
}

function refreshMessages() {
  const currentChannel = getCurrentChannel()

  getJSON('/api/channel/' + currentChannel, updateMessageHTML)
}

async function sendMessage() {
  const message = messageInput.value

  if (message === '') {
    return
  }

  const currentChannel = getCurrentChannel()

  const messageData = {
    channel: currentChannel,
    name: 'Sam',
    msg: message,
  }

  await postJSON('/api/send_message', messageData)

  messageInput.value = ''
}

getJSON('/api/channels', updateChannelList)
refreshMessages()

setInterval(refreshMessages, 1000)

messageInput.onkeypress = (e) => {
  if (!e) {
    e = window.event
  }

  const keyCode = e.code || e.keyCode

  if (keyCode == 'Enter') {
    sendMessage()
  }
}
