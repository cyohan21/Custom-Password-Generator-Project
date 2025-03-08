# Python Custom Password Generator 

Welcome to my first ever python project! This will be a brief overview and rundown of how my custom password generator works.

## Overview

This is a python custom password generator. This program will give you a random password with customization and diversity. All passwords will have a variety of standard characters (uppercase, lowercase, numbers and symbols) with the option to choose a password length between 8-32.
You also have the option to add chinese, japanese, and greek characters if you wish.

## How It Works

When you initialize the program, you will be introduced with the following prompt:

***Welcome to the random password generator!
Please enter either 1 to generate a random password, or 2 to customize the randomization (type 'exit' to quit):***

If the input given is 1, the program will generate a random 8 letter password with standard characters.

If the input given is 2, the program will ask the following:


***Enter Custom Password Length in range from 8-32...***

If the input given is out of range, you will be prompted with an error.

***Custom length must be in range from 8-32 characters...***

Once given an input in range, such as '30', you will then be given the option to choose:

***Do you want to use standard characters(1) or custom characters (2)?***

The input '1' will give you a randomization of standard characters within the set custom length.
The input '2' will further prompt you to the following 'yes/no questions:


***Do you want Greek characters? (yes or no)***

***Do you want Japanese characters? (yes or no)***

***Do you want Chinese characters? (yes or no)***

Once all inputs are given, your password will be generated!

***Generated custom password: cぞ%87ξn,,0ゕ泞蠡ごO34OfNαPをτ蘽ゃsa1α***



## Update: 

Error fixed when input was 'no' on prompt "Do you want Chinese characters? (yes/no)". 


End of line 16 changed from nested list [[]] to list []





