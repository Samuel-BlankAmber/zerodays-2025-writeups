# Secret Phrase

The password is the flag, with the secret message encrypted being `gulqnbgulqn$`.

This is computed by taking each decimal value of the flag message, adding 3, and converting it back to the character.

This is reversible:
`"".join(chr(ord(c)-3) for c in "gulqnbgulqn$")`
`'drink_drink!'`

The flag is: `ZeroDays{drink_drink!}`
