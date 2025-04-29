class ElementoListaPonderada {
    constructor(value, weight){
        this.value = value
        this.weight = weight
    }
}

function sumSquareDiff(data, paramToCompare){
    let acumulator = 0
    for(let value of data){
        acumulator += (value - paramToCompare)**2
    }

    return acumulator
}

function summatory(data){
    let acumulator = 0
    for(let value of data){
        acumulator += value
    }

    return acumulator
}

function mediaPonderada(listaPonderada) {
    let sumWeight = 0
    let sum = 0
    for(let item of listaPonderada){
        sumWeight += item.weight
        sum += item.value * item.weight
    }
    return sum / sumWeight
}

function variancia(data) {
    return sumSquareDiff(data, summatory(data) / data.length) / data.length
}
function desvioPadrao(data) {
    return variancia(data)**0.5
}

const opcoes = {
    "1": mediaPonderada,
    "2": variancia,
    "3": desvioPadrao
}

listaPonderada = [
    new ElementoListaPonderada(9, 0.3),
    new ElementoListaPonderada(8.7, 0.3),
    new ElementoListaPonderada(9.7, 0.4)
]

function rowDice(dice){
    dice = dice.split('d')
    let acumulator = 0
    let quantity = dice[0]
    let surfaces = dice[1]
    for(let i = 0; i < quantity; i++){
        value = Math.floor(Math.random()*diceType) + 1
        acumulator += value
    }
    return acumulator
}

const data = []

const diceType = "7d4"

function feedData(data, qtdData=200){
    for(let i=0; i < qtdData; i++){
        data.push(rowDice('12d10'))
    }
}

feedData(data, 700)

let a = opcoes["1"](listaPonderada)
let b = opcoes["2"](data)
let c = opcoes["3"](data)


console.log(`Média Ponderada:${a}`)

console.log(`Variância: ${b}`)

console.log(`Desvio padrão: ${c}`)

console.log(data)


function generateFreqGraph(data){
    data.sort()
    let min = data[0]
    let max = data[data.length - 1]
    
    for(let i = min; i < max; i++){
        let freq = many(i, data)
        let tempStr = ''
        for(let j = 0; j < freq; j++){
            tempStr += "#"
        }
        console.log(`${i} | ${tempStr}`)
    }
}

function many(value, list){
    let aux = 0
    for(let el of list){
        if (el == value){
            aux++
        }
    }
    return aux
}

generateFreqGraph(data)

// let a = rowDice('12d10')

// console.log(a)