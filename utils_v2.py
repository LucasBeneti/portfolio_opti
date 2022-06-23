import numpy as np
from scipy import optimize 

# @ param etaClassification - classificacao das stocks entre alta volatilidade e baixa volatilidade
# @ param ighLowVolatUpperBounds - limites superiores para a constraint de volatilidade (ex: 60%,40% - proporcao de baixa volat e alta volat)
# @ param ighLowVolatLowerBounds - limites inferiores para constraint de volatilidade (ex: 1%,1% - proporcao de baixa volat e alta volat)
# @ param oundariesByBeta - limites maximos sabendo os valores dos betas
def SLSQPSSolver(meanReturns, covarianceReturns, riskAverseParam, portifolioSize, betaClassification, boundariesByBeta):
    # definicao da funcao objetivo
    def fo(x, meanReturns, covarianceReturns, riskAverseParam, portifolioSize):
        PortfolioVariance = np.matmul(np.matmul(x, covarianceReturns), x.T) 
        PortfolioExpReturn = np.matmul(np.array(meanReturns),x.T)
        func = riskAverseParam * PortfolioVariance - (1-riskAverseParam)*PortfolioExpReturn
        return func
    
    def ConstraintIneqUpBounds(x):
        A = betaClassification
        bUpBounds = np.array([0.7,0.3]).T
        constraintValUpBounds = bUpBounds-np.matmul(A,x.T) 
        return constraintValUpBounds

    def ConstraintIneqLowBounds(x):
        A = betaClassification
        bLowBounds = np.array([0.01, 0.01]).T
        constraintValLowBounds = np.matmul(A,x.T)-bLowBounds  
        return constraintValLowBounds

    cons = ({'type': 'eq', 'fun': lambda x: np.sum(x)-1}, \
            {'type':'ineq', 'fun': ConstraintIneqUpBounds},\
            {'type':'ineq', 'fun': ConstraintIneqLowBounds})
    
    optResponse = optimize.minimize(fo, x0 = np.repeat(0.01, portifolioSize), args = (meanReturns, covarianceReturns, riskAverseParam, portifolioSize), method = 'SLSQP',  bounds = boundariesByBeta, constraints = cons, tol = 10**-3)
    print("***** Version: 0.0.4 tol**-3 *****")
    print(optResponse)
    return optResponse


# betaBoundaries - lista com limites para low e high volat respectivamente (ex: [0.1, 0.01]
def getVolatilityArr(beta, betaBoundaries):
    [lowVolatBound, highVolatBound] = betaBoundaries
    volArr = [[],[]]
    boundaries = []
    counter = 0
    for res in beta:
        if(res >= 1):
            volArr[0].append(0)
            volArr[1].append(1)
            boundaries.append((0, highVolatBound))
        else:
            volArr[0].append(1)
            volArr[1].append(0)
            boundaries.append((0, lowVolatBound))
    return [volArr, boundaries]