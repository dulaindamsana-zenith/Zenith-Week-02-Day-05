#========================================= ### ZENITH ENCRYPTOR ### =========================================#
#
# INFO:
#       A WORD ENCRYPTOR THAT CAN"T EVEN BREAK BY CURRENT QUANTUM COMPUTERS
#       LANGUAGE: PYTHON
#       CONTRIBUTOR: COLABAGE DULAIN DAMSANA
#       FUTRUE AMB: QUANTUM CYBER PHICYST
#       COURSE NAME: ZENITH

# Importaions
import zenith_encryptor

# Anci Colors
BACKGROUND_RED = "\033[91m\033[7m"
BACKGROUND_GREEN = "\033[92m\033[7m"
BACKGROUND_YELLOW = "\033[93m\033[7m"
BACKGROUND_BLUE = "\033[94m\033[7m"
BACKGROUND_PURPLE = "\033[95m\033[7m"
BACKGROUND_CYAN = "\033[96m\033[7m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

banner_UP_DOWN_width = 160 * "="
banner_CENTER_FIRST_width = 64 * "="
banner_CENTER_LAST_width = 63 * "="

print(f"{BACKGROUND_GREEN}{banner_UP_DOWN_width}{RESET}")
print(f"{BACKGROUND_GREEN}{banner_CENTER_FIRST_width} WELCOME TO THE ZENITH ENCRYPTOR {banner_CENTER_LAST_width}{RESET}")
print(f"{BACKGROUND_GREEN}{banner_UP_DOWN_width}{RESET}\n\n ")

try:
        user_text = input(f"{BLUE}[?] Enter the message you want to encrypt via {YELLOW}ZENITH ENCRYPTOR:{RESET}\n\n{PURPLE}")
        print("\n", 160 * "-")
        encrypt_method = input(f"""
{BLUE}[?] Enter the {YELLOW}encryption{RESET}{BLUE} method you want to use:

1. AES (Advanced Encryption Standard) == enter 1
2. RSA (Rivest - Shamir - Adleman) == enter 2
3. UTF - 8 (Unicode Transformation Format) == enter 3
{RESET}\n{PURPLE}
""")
except Exception as e:
        print(f"\n\n{BACKGROUND_RED}ERROR_1:{RESET}{RED} Uknown Error")
        exit()

if encrypt_method == "1":
        encrypted_text = zenith_encryptor.aes_encrypt(user_text)
        print(f"\n\n{BACKGROUND_CYAN}Entered Text: \n\n{RESET}{CYAN}{user_text}{RESET}")
        print(f"\n{BACKGROUND_YELLOW}Encrypted Text: \n\n{RESET}{YELLOW}{encrypted_text}{RESET}")
        print(f"\n{BACKGROUND_PURPLE}[!!!] MISSION ACOUMPLISHED [!!!]{RESET}")
        exit()

elif encrypt_method == "2":
        encrypted_text = zenith_encryptor.rsa_encrypt(user_text)
        print(f"\n\n{BACKGROUND_CYAN}Entered Text: \n\n{RESET}{CYAN}{user_text}{RESET}")
        print(f"\n{BACKGROUND_YELLOW}Encrypted Text: \n\n{RESET}{YELLOW}{encrypted_text}{RESET}")
        print(f"\n{BACKGROUND_PURPLE}[!!!] MISSION ACOUMPLISHED [!!!]{RESET}")
        exit()

elif encrypt_method == "3":
        encrypted_text = zenith_encryptor.utf_8_encrypt(user_text, )
        print(f"\n\n{BACKGROUND_CYAN}Entered Text: \n\n{RESET}{CYAN}{user_text}{RESET}")
        print(f"\n{BACKGROUND_YELLOW}Encrypted Text: \n\n{RESET}{YELLOW}{encrypted_text}{RESET}")
        print(f"\n{BACKGROUND_PURPLE}[!!!] MISSION ACOUMPLISHED [!!!]{RESET}")
        exit()

else:
        print(f"\n\n{BACKGROUND_RED}ERROR_2:{RESET}{RED}ENCRYPTING METHOD NOT FOUND{RESET}")
        print(f"\n {BACKGROUND_RED}[!⸮!] MISSION UNACHIEVED [!?!]{RESET}")
        exit()