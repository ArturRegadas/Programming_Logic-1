while(num:=input("digite um numero, p-parar: "))!='p':soma=0 if not 'soma' in globals() else soma;f1=0 if not 'f1' in globals() else f1;f2=0 if not 'f2' in globals() else f2;f3=0 if not 'f3' in globals() else f3;f4=0 if not 'f4' in globals() else f4;f5=0 if not 'f5' in globals() else f5;par=0 if not 'par' in globals() else par;imp=0 if not 'imp' in globals() else imp;n=1 if not 'n' in globals() else n;nu=int(num);soma+=nu;print(f"A media atualmente é {soma/n}");maior = float('inf')*-1 if not 'maior' in globals() else maior;maior = nu if nu > maior else maior;print(f"O maior numero Ate agora foi {maior}");print("O numero {nu} esta na faixa: ", end='');f1+=1 if nu < 0 else 0;print("1\n"if nu < 0 else '', end='');f2+=1 if nu >=0 and nu < 15 else 0;print('2\n' if nu>=0 and nu < 15 else '', end='' );f3+=1 if nu >=15 and nu < 100 else 0;print('3\n' if nu >=15 and nu < 100 else '', end='');f4+=1 if nu >= 1000 else 0;print('4\n' if nu > 1000 else '', end='');f5+=1 if nu >=101 and nu < 1000 else 0;print('5\n'if nu >=101 and nu < 1000 else '', end='');print(f"Ao todo foram:\nfaixa 1: {f1}\nfaixa 2: {f2}\nfaixa 3: {f3}\nfaixa 4: {f4}\nfaixa 5: {f5}");par += 1 if nu % 2==0 else 0;imp += 1 if nu %2 !=0 else 0;print(f"O numero {nu} é ", end='');print("par" if nu % 2 ==0 else 'impar');print(f"Ao todo foram {par} numero pares e {imp} numeros Impares");print("\n")