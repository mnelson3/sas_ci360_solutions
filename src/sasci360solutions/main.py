#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import configparser
from configparser import ConfigParser
from pathlib import Path

from sasci360apimarketinggateway.agents import Agents
from sasci360apimarketinggateway.configuration import Configuration
from sasci360apimarketinggateway.data_download import DataDownload
from sasci360apimarketinggateway.events import Events
from sasci360apimarketinggateway.root import Root


class Main:

	def __init__(self):
		config_parser = ConfigParser(interpolation=configparser.ExtendedInterpolation())
		config_file = Path("{0}{1}".format("/Users/manels/Repositories/sas_ci360_solutions/config/", "config.ini"))
		config_parser.read(config_file)

		self.algorithm = config_parser.get("GENERAL", "algorithm")
		self.api = config_parser.get("GENERAL", "api")
		self.encoding = config_parser.get("GENERAL", "encoding")
		self.host = config_parser.get("GENERAL", "host")
		self.secret_key = config_parser.get("GENERAL", "secret_key")
		self.tenant_id = config_parser.get("GENERAL", "tenant_id")

		print(self.algorithm)
		print(self.api)
		print(self.encoding)
		print(self.host)
		print(self.secret_key)
		print(self.tenant_id)

		self.agents = Agents(algorithm=self.algorithm, api=self.api, encoding=self.encoding, host=self.host, secret_key=self.secret_key, tenant_id=self.tenant_id)
		self.configuration = Configuration(algorithm=self.algorithm, api=self.api, encoding=self.encoding, host=self.host, secret_key=self.secret_key, tenant_id=self.tenant_id)
		self.data_download = DataDownload(algorithm=self.algorithm, api=self.api, encoding=self.encoding, host=self.host, secret_key=self.secret_key, tenant_id=self.tenant_id)
		self.events = Events(algorithm=self.algorithm, api=self.api, encoding=self.encoding, host=self.host, secret_key=self.secret_key, tenant_id=self.tenant_id)
		self.root = Root(algorithm=self.algorithm, api=self.api, encoding=self.encoding, host=self.host, secret_key=self.secret_key, tenant_id=self.tenant_id)


if __name__ == "__main__":
	Main()
