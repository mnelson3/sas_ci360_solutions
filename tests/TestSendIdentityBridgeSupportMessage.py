#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

from sasci360solutions import identity_data


def test_send_identity_bridge_support_message_mode_development():
	mode = "development"
	custom = identity_data.SendIdentityBridgeSupportMessage.SendIdentityBridgeSupportMessage(mode=mode)
	result = custom.run()
	print("result : {0}".format(result))
	assert result is None


def test_send_identity_bridge_support_message_mode_test():
	mode = "test"
	custom = identity_data.SendIdentityBridgeSupportMessage.SendIdentityBridgeSupportMessage(mode=mode)
	result = custom.run()
	print("result : {0}".format(result))
	assert result is None


def test_send_identity_bridge_support_message_mode_production():
	mode = "production"
	custom = identity_data.SendIdentityBridgeSupportMessage.SendIdentityBridgeSupportMessage(mode=mode)
	result = custom.run()
	print("result : {0}".format(result))
	assert result is None


def test_send_identity_bridge_support_message():
	custom = identity_data.SendIdentityBridgeSupportMessage.SendIdentityBridgeSupportMessage()
	result = custom.run()
	print("result : {0}".format(result))
	assert result is None
