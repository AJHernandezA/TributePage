

# lIndex = [9, 8, 13, 25, 24, 4, 19, 10, 2, 15]
# lCateg = [8, 8, 6, 6, 3, 5, 3, 3, 1, 3, 7, 6, 6, 1, 1, 6, 7, 1, 6, 2, 2, 6, 5, 4, 8, 4, 8, 2, 4, 6]
# nomCateg = 6
# result=[]   
# pos=0
# numero=0
# rep = 0
# for i in lCateg:
#                 if i == nomCateg:
#                     rep = lCateg.count(nomCateg)
#                     break
#                 numero+=1
# pos = lIndex[numero]
# result = [pos,rep]    
# print(result)

l1 = [12, 26, 13, 22, 39, 40, 25, 47, 48, 10, 17, 7, 15, 31, 4, 35, 0, 29, 36]
l2 = [29, 5, 11, 18, 19, 16, 26, 25, 9, 17, 38, 37, 20, 35, 23, 24, 40, 34]
# result = []
# con=0
# for i in lBodega2:
#     if i not in lBodega1:
#            result.append(i)
# print(result)

def retornaParaIntercambio(lBodega1, lBodega2):
        result = []
        for i in lBodega2:
            if i not in lBodega1:
                result.append(i)
        return result

print(retornaParaIntercambio(l1, l2))
# def retornaCantidadIntercambio(lBodega1, lBodega2):

