# XLR HipChat Plugin #

[![Build Status](https://travis-ci.org/xebialabs-community/xlr-hipchat-plugin.svg?branch=master)](https://travis-ci.org/xebialabs-community/xlr-hipchat-plugin)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/4e2e745bad74407ab3484176d3246d79)](https://www.codacy.com/app/erasmussen39/xlr-hipchat-plugin?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=xebialabs-community/xlr-hipchat-plugin&amp;utm_campaign=Badge_Grade)
[![Code Climate](https://codeclimate.com/github/xebialabs-community/xlr-hipchat-plugin/badges/gpa.svg)](https://codeclimate.com/github/xebialabs-community/xlr-hipchat-plugin)
[![License: MIT][xlr-hipchat-plugin-license-image]][xlr-hipchat-plugin-license-url]
[![Github All Releases][xlr-hipchat-plugin-downloads-image]]()

[xlr-hipchat-plugin-license-image]: https://img.shields.io/badge/License-MIT-yellow.svg
[xlr-hipchat-plugin-license-url]: https://opensource.org/licenses/MIT
[xlr-hipchat-plugin-downloads-image]: https://img.shields.io/github/downloads/xebialabs-community/xlr-hipchat-plugin/total.svg


## Preface
This document describes the functionality provided by the `xlr-hipchat-plugin`

## Overview
This module offers a basic interface to HipChat functionality.

## Installation
Sewe [here](https://docs.xebialabs.com/xl-release/how-to/install-or-remove-xl-release-plugins.html)

## HipChat Authentication
Configures the credentials used to authenticate with the HipChat REST API. You should use the API access token configured in your[HipChat](https://www.hipchat.com/account/api)account. Note that the token needs to have both the "send_message" and "send_notification" scopes available. 

![HipChatAuthenticationConfiguration](images/HipChatAuthenticationConfiguration.png)

## Available Tasks
The available tasks for interfacing with HipChat. These tasks utilize the HipChat REST API and the provided HipChat Authentication Configuration.

### Notify Room
Sends the specified notification to a list of specified rooms (name or ID).

![HipChatNotifyRoom](images/HipChatNotifyRoom.png)

### Message User
Sends the specified message to a list of specified users (@ReferenceName, ID, or email).

![HipChatMessageUser](images/HipChatMessageUser.png)

--- 

## References:
* [HipChat REST API](https://www.hipchat.com/docs/apiv2)
