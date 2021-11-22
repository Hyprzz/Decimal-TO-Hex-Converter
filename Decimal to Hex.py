userInput = input("[+] Input a integer to be converted: ")

try:
  val = int(userInput)
  hexnum = hex(val)
  print(f"[+] The number {val} converted to hex is {hexnum}")

  decnum = int(hexnum, 16)
  print(f"[+] Hex {hexnum} Converted back to decimal it is {decnum}")

except ValueError:
  print("[!] Please input a valid integer!")

