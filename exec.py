import random

def generate_custom_pass(length, use_standard_chars=True, greek_inc=False, jap_inc=False, chinese_inc=False):

    # standard characters

    lower_chars = [chr(random.randint(97, 122)) for _ in range(length//4)] # length//4 ensures diversity between characters
    upper_chars = [chr(random.randint(65, 90)) for _ in range(length//4)]
    nums = [chr(random.randint(48, 57)) for _ in range(length//4)]
    symbls = [chr(random.randint(33, 47)) for _ in range(length//4)]

    # custom characters

    greek_chars = [chr(random.randint(945, 969)) for _ in range(length//4)] if greek_inc else [] # requires that the user accepts custom characters as input
    jap_chars = [chr(random.randint(12353,12438)) for _ in range(length//4)] if jap_inc else []
    chinese_chars = [chr(random.randint(0x4e00, 0x9fff)) for _ in range(length//4)] if chinese_inc else []

    if use_standard_chars:
        all_chars = lower_chars + upper_chars + nums + symbls
    else:
        all_chars = lower_chars + upper_chars + nums + symbls + greek_chars + jap_chars + chinese_chars

    random.shuffle(all_chars)
    password = ''.join(all_chars[:length]) # slice the list and combine it all into one string, restricted to the length given.
    return password

def get_valid_input(messages, valid_responses, exit_avail=False):
    while True:
        user_input = input(messages).strip().lower() # Error handling for whitespace and case sensitivity
        if user_input == 'exit' and exit_avail: # ensures they can only exit when permissible.
            print('Bye Bye!')
            exit()
        elif user_input in valid_responses:
            return user_input
        else:
            print("I didn't get that, please try again.")

while True:
    welcome_input = get_valid_input("""Welcome to the random password generator!
Please enter either 1 to generate a random password, or 2 to customize the randomization (type 'exit' to quit): """,
                                    ['1', '2'], exit_avail=True)

    if welcome_input == '1':
        print('Generated Random Password:', generate_custom_pass(8)) # will always generate a password with at least 8 characters
    elif welcome_input == '2':
        custom_length = int(input('Enter Custom Password Length in range from 8-32...'))
        while custom_length < 8 or custom_length > 32: # User cannot continue without the custom length in valid range.
            print('Custom length must be in range from 8-32 characters...')
            custom_length = int(input('Enter Custom Password Length in range from 8-32...')) # Call back the input again.

        char_choice = get_valid_input('Do you want to use standard characters(1) or custom characters (2)?',['1', '2'])
        if char_choice == '1':
            print('Generated custom password with standard characters:', generate_custom_pass(custom_length, use_standard_chars = True))
        elif char_choice == '2':
            include_greek = get_valid_input('Do you want Greek characters? (yes or no)', ['yes', 'no']) == 'yes' # yes turns the input True.
            include_japanese = get_valid_input('Do you want Japanese characters? (yes or no)', ['yes', 'no']) == 'yes'
            include_chinese = get_valid_input('Do you want Chinese characters? (yes or no)', ['yes', 'no']) == 'yes'

            print('Generated custom password:', generate_custom_pass(
                custom_length,
                use_standard_chars=False,
                greek_inc = include_greek, # update the input given by the user.
                jap_inc = include_japanese,
                chinese_inc = include_chinese
            ))
    break