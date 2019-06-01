mov 0xffff, 1
mov D, 2
mov A, D
mov 0xfeee, A
add A, D
add 0xfeee, 10
lbl loop
inc A
jmp loop, A=100
imul B, D, D
inc 0xffff
imul C, D, 0xffff