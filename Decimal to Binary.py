#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Decimal to Binary.py
#  
#  Copyright 2013 GamiShin ZenOokami <GamiShin ZenOokami@GAMISHINZENOOKA>
#  www.EssenceOfZen.Tk
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


# Basically create a program that divides a number by 2 until it reaches
# 0 and then append to a list in that order, once that list is finished
# flip the list backwards in order to display the correct binary number.

#==Global Variables==#
version = "0.0.1"
dev_team = ["ZenOokami"]
last_updated = "June 5th, 2013"


def mode_menu():
	print("#===========================================#")
	print("#Menu Under Construction for Later Update   #")
	print("#===========================================#")

def decimal_to_binary_convert(number):
	binary_list = [] # We create an empty list ahead of time.
	old_number = number # For reference
	while (number > .5): # We setup our loop to finish out an entire conversion.
		if number % 2 != 0: # If a number/2 = a number and 1/2 
			binary_list.append(1)
		else:
			binary_list.append(0) # If a number is a whole number.				
		number /= 2 #  Divide the starting nubmer by 2
		number = int(number) # Get rid of the .5 if there is one.
		print(binary_list) # Check to see if it's working
		print()
	print("The Binary form for " + str(old_number) + " is: ")
	print(binary_list[::-1]) # Print the binary list backwards to show correctly.

def main():
	print("Welcome to EoZ's Decimal to Binary converter!")
	switch = 0
	while (switch == 0):
		number = int(input("Plase input a decimal number to convert: "))
		decimal_to_binary_convert(number) # Call our function 
		print()
		question = 1
		while(question == 1):
			user_response = input("Are you finished? Yes or No: ").lower()
			print()
			if user_response == "yes":
				switch = 1
				question = 0
			elif user_response == "no":
				switch = 0
				question = 0
			else:
				print("Invalid answer, try again")
				question = 1
	print("Thank you for using our program")
	print("version: " + str(version))
	print("Last Update: " + last_updated )
	
main()
		
