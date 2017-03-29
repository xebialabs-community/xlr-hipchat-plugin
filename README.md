# XLR HipChat Plugin #

[![Build Status](https://travis-ci.org/xebialabs-community/xlr-hipchat-plugin.svg?branch=master)](https://travis-ci.org/xebialabs-community/xlr-hipchat-plugin)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/4e2e745bad74407ab3484176d3246d79)](https://www.codacy.com/app/erasmussen39/xlr-hipchat-plugin?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=xebialabs-community/xlr-hipchat-plugin&amp;utm_campaign=Badge_Grade)
[![Code Climate](https://codeclimate.com/github/xebialabs-community/xlr-hipchat-plugin/badges/gpa.svg)](https://codeclimate.com/github/xebialabs-community/xlr-hipchat-plugin)

## Preface
This document describes the functionality provided by the `xlr-hipchat-plugin`

## Overview
This module offers a basic interface to HipChat functionality.

## Installation
Copy the plugin JAR file into the `SERVER_HOME/plugins` directory of XL Release.

## HipChat Authentication
Configures the credentials used to authenticate with the HipChat REST API. You should use the API access token configured in your[HipChat](https://www.hipchat.com/account/api)account. 

![HipChatAuthenticationConfiguration](images/HipChatAuthenticationConfiguration.png)

## Available Tasks
The available tasks for interfacing with HipChat. These tasks utilize the HipChat REST API and the provided HipChat Authentication Configuration.

### Send Room Notification
Sends the specified notification message to the specified room.

![HipChatSendRoomNotification](images/HipChatSendRoomNotification.png)

--- 

## References:
* [HipChat REST API](https://www.hipchat.com/docs/apiv2)
