const allBtnHTML = document.querySelectorAll('button')

allBtnHTML.forEach((el) => {
    el.addEventListener('mouseenter', (e) => {
        console.log("Hover detected")
        console.log(el)
        el.style.borderColor = getRandomColor()
        el.style.backgroundColor = getRandomColor()
        el.style.color = getRandomColor()
        el.innerText = getRandomLetter()
    })


    el.addEventListener('click', (e) => {
        console.log("Click detected")
        console.log(el)
        el.style.borderColor = ''
        el.style.backgroundColor = ''
        el.style.color = ''
        el.innerText = ''
    })
})



function getRandomColor(){
    return `rgb(${getRandomInt(255)}, ${getRandomInt(255)}, ${getRandomInt(255)})`
}

function getRandomInt(max){
    return Math.floor(Math.random()*max)
}

function getRandomLetter(){
    let str = 'QWERTYUIOPASDFGHJKLÇZXCVBNM'
    return str[getRandomInt(str.length - 1)]
}