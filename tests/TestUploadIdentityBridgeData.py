#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

from sasci360solutions import identity_data


def test_upload_identity_bridge_data_mode_development():
	mode = "development"
	custom = identity_data.UploadIdentityBridgeData.UploadIdentityBridgeData(mode=mode)
	result = custom.run()
	print("result : {0}".format(result))
	assert result is not None


def test_upload_identity_bridge_data_mode_test():
	mode = "test"
	custom = identity_data.UploadIdentityBridgeData.UploadIdentityBridgeData(mode=mode)
	result = custom.run()
	print("result : {0}".format(result))
	assert result is not None


def test_upload_identity_bridge_data_mode_production():
	mode = "production"
	custom = identity_data.UploadIdentityBridgeData.UploadIdentityBridgeData(mode=mode)
	result = custom.run()
	print("result : {0}".format(result))
	assert result is not None


def test_upload_identity_bridge_data():
	custom = identity_data.UploadIdentityBridgeData.UploadIdentityBridgeData()
	result = custom.run()
	print("result : {0}".format(result))
	assert result is not None
