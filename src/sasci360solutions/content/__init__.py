#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

from sasci360solutions.main import Main


class Content(Main):
	"""
	Content Module
	"""

	def __init__(self) -> None:
		super().__init__()

		print("Content-Result: {}".format(self.algorithm))


if __name__ == "__main__":
	Content()
