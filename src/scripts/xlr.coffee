# Description:
#   Interact with XLR
#
# Commands:
#   @ClarkHubot release templateId 4.0.5
module.exports = (robot) ->
  url = process.env.HUBOT_XLRELEASE_URL
  notifyUrl = process.env.HUBOT_XLRELEASE_NOTIFY_URL
  auth = 'Basic ' + new Buffer(process.env.HUBOT_XLRELEASE_AUTH).toString('base64')

  startRelease = (msg, releaseId, data) ->
    robot.http("#{url}/api/v1-beta/templates/Applications/#{releaseId}/start")
      .headers(Authorization: auth, Accept: 'application/json', 'Content-Type': 'application/json')
      .post(data) (err, res, body) ->
        if (err)
          msg.send "Error! Please have a look at Heroku's logs"
        else
          release = JSON.parse body
          msg.send "Started release : #{url}/#/releases/#{release.id.replace(/Applications\//, '')}"


  robot.respond /release (.*)/i, (msg) ->
    room = msg.envelope.user.reply_to

    templateID = msg.match[1]
    version = msg.match[2]
    console.log "Releasing version : #{version}"

    data = JSON.stringify
      releaseTitle: "Release from HipChat #{version}",
      releaseVariables:
        '${version}': version
        '${notifyURL}': "#{notifyUrl}"
        '${room}': room

    startRelease msg, templateID, data


  robot.router.post '/hubot/messageToRoom', (req, res) ->
    robot.messageRoom req.body.room, "XL Release says: #{req.body.message}"
    res.send 'OK'
