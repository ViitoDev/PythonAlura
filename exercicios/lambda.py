operacoes = { 
    '+': soma,  
    '-': subtrai, 
    '*': multiplica, 
    '/': divide
} 

if operacao in operacoes:  
   resultado = operacoes[operacao](x, y)  
   print(f"O resultado é: {resultado}")  

else:  
   print("Operação inválida") 
