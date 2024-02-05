#Esforços são as expressões com esforços solicitantes

#Exercício 1 (2 da lista)
def forcas1 (Comprimento, Carregamento):
    forca_resultante = Comprimento * Carregamento
    forca_do_apoio = - forca_resultante
    return(forca_resultante, forca_do_apoio)
def esforcos1 (carregamento, distanciaCorte):
    cortante = int(carregamento*distanciaCorte)
    momentoCarregado = int(cortante *distanciaCorte/2)
    return cortante, momentoCarregado

#Exercício 2 (3 da lista)
def forcas2 (comprimento, carregamento):
    forca_resultante = (comprimento * carregamento)/2
    forca_de_apoio = - forca_resultante
    return(forca_resultante, forca_de_apoio)
def esforcos2 (carregamento, comprimento_barra, distanciaCorte):
    forcaInterna = carregamento/comprimento_barra*distanciaCorte
    cortante = int(forcaInterna*distanciaCorte/2)
    momentoCarregado = int(cortante * distanciaCorte/3)
    return cortante, momentoCarregado

#Exercício 3 (8 da lista)
def forcas3 (momento_dado, comprimento):
    Forca_de_apoioA = momento_dado/comprimento
    Forca_de_apoioB = - Forca_de_apoioA
    return (Forca_de_apoioA, Forca_de_apoioB)
def esforcos3 (Forca_de_apoioB, comprimento, distanciaCorte): ##Reação do apoio vem da expressão que calcula o apoio
    momentoCarregado = int(Forca_de_apoioB*(comprimento - distanciaCorte))
    return momentoCarregado

#Exercício 4 (9 da lista)
def forcas4 (Momento_dado, Carregamento, Comprimento_da_barra):
    Forca_de_apoioA = (Carregamento * Comprimento_da_barra)/2 + Momento_dado/Comprimento_da_barra
    Forca_de_apoioB = (Carregamento * Comprimento_da_barra/2) - Momento_dado/Comprimento_da_barra
    return(Forca_de_apoioA, Forca_de_apoioB)

def esforcos4 (Carregamento, distanciaCorte, Momento_dado, comprimentoBarra):
    cortante = (Carregamento * comprimentoBarra)/2 - (Momento_dado/comprimentoBarra) - (Carregamento * distanciaCorte)
    momentoCarregado = ((Carregamento * comprimentoBarra)/2 - (Momento_dado / comprimentoBarra))*distanciaCorte - (Carregamento * (distanciaCorte**2))/2
    return cortante, momentoCarregado

#Exercício 5 (10 da lista)
def forcas5 (Carregamento, forca_f2, Comprimento, distanciaf2_ao_pontoA):
    Forca_de_apoioA = (forca_f2 * (Comprimento - distanciaf2_ao_pontoA))/Comprimento + Carregamento * Comprimento/2
    Forca_de_apoioB = (forca_f2 * (distanciaf2_ao_pontoA))/Comprimento + Carregamento * Comprimento/2
    Resultante = Carregamento * Comprimento
    return(Forca_de_apoioA, Forca_de_apoioB, Resultante) 
def esforcos5 (forca, distanciaCorte, comprimento, carregamento, distanciaf2_ao_pontoA):
    cortante = forca*(comprimento - distanciaf2_ao_pontoA)/comprimento + carregamento*comprimento/2 - forca*distanciaCorte
    momentoFletor = (forca*(comprimento - distanciaf2_ao_pontoA)/comprimento + carregamento*comprimento/2)*distanciaCorte - (forca*distanciaCorte**2)/2
    return cortante, momentoFletor

#Exercício 6 (11 da lista)
def forcas6 (comprimento_d1, comprimento_d2, comprimento_d3, carregamento):
    comprimento_da_barra = comprimento_d1 + comprimento_d3 + comprimento_d2
    
    resultante = carregamento * comprimento_d2
    ponto_de_aplicacao = comprimento_d1 + comprimento_d2/2
    
    Forca_de_apoioA = (resultante * ponto_de_aplicacao)/comprimento_da_barra
    Forca_de_apoioB = (resultante * (comprimento_da_barra - ponto_de_aplicacao))/comprimento_da_barra
    
    return (Forca_de_apoioA, Forca_de_apoioB)

def esforcos6 (carregamento, Forca_de_apoioB, comprimento_d3, distanciaCorte, comprimento_d2, comprimento_d1): ##Reação do apoio vem da expressão que calcula o apoio
    comprimentoBarra = comprimento_d1 + comprimento_d3 + comprimento_d2

    if (distanciaCorte < comprimento_d1 + comprimento_d2):
        cortante = int(carregamento * (distanciaCorte - comprimento_d2 ) + Forca_de_apoioB)
    else:
        cortante = int(carregamento * comprimento_d2 + Forca_de_apoioB)

    momentoCarregado = int((cortante + Forca_de_apoioB)*(comprimentoBarra - distanciaCorte))
    return momentoCarregado, cortante