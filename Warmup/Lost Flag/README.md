# Lost Flag

## Solution 1

1. `gdb chall`
2. `main`
3. `b *(main+699)`
4. `run`
5. `telescope` or `x/s $rdi`

Flag is visible in the stack: `ZeroDays{char_by_char_we_all_fall_down}`

## Solution 2

Patch binary, replace `call free` with `call puts`.
Run patched binary.
