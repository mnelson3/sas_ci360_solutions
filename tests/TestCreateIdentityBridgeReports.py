#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

from sasci360solutions import identity_data


def test_create_identity_bridge_reports_mode_development():
	mode = "development"
	custom = identity_data.CreateIdentityBridgeReports.CreateIdentityBridgeReports(mode=mode)
	result = custom.run()
	print("result : {0}".format(result))
	assert result is None


def test_create_identity_bridge_reports_mode_test():
	mode = "test"
	custom = identity_data.CreateIdentityBridgeReports.CreateIdentityBridgeReports(mode=mode)
	result = custom.run()
	print("result : {0}".format(result))
	assert result is None


def test_create_identity_bridge_reports_mode_production():
	mode = "production"
	custom = identity_data.CreateIdentityBridgeReports.CreateIdentityBridgeReports(mode=mode)
	result = custom.run()
	print("result : {0}".format(result))
	assert result is None


def test_create_identity_bridge_reports():
	custom = identity_data.CreateIdentityBridgeReports.CreateIdentityBridgeReports()
	result = custom.run()
	print("result : {0}".format(result))
	assert result is None
