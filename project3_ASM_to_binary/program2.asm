addi $1,$0,0
addi $2,$0,5
addi $3,$0,0
addi $6,$0,0
beq $2,$3,48
add $4,$3,$3
add $4,$4,$4
add $4,$1,$4
lw $5,0($4)
add $6,$6,$5
addi $3,$3,1
beq $0,$0,-32
sw $6,40($1)
