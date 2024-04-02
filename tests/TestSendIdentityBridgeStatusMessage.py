#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

from sasci360solutions import identity_data


def test_send_identity_bridge_status_message_mode_development():
	mode = "development"
	file_name = "import_request_jobs_get_20200527160403"
	custom = identity_data.SendIdentityBridgeStatusMessage.SendIdentityBridgeStatusMessage(mode=mode)
	result = custom.run(file_name=file_name)
	print("result : {0}".format(result))
	assert result is None


def test_send_identity_bridge_status_message_mode_test():
	mode = "test"
	file_name = "import_request_jobs_get_20200527160332"
	custom = identity_data.SendIdentityBridgeStatusMessage.SendIdentityBridgeStatusMessage(mode=mode)
	result = custom.run(file_name=file_name)
	print("result : {0}".format(result))
	assert result is None


def test_send_identity_bridge_status_message_mode_production():
	mode = "production"
	file_name = ""
	custom = identity_data.SendIdentityBridgeStatusMessage.SendIdentityBridgeStatusMessage(mode=mode)
	result = custom.run()
	print("result : {0}".format(result))
	assert result is None


def test_send_identity_bridge_status_message():
	custom = identity_data.SendIdentityBridgeStatusMessage.SendIdentityBridgeStatusMessage()
	result = custom.run()
	print("result : {0}".format(result))
	assert result is None
