// titulo
// capa
// score

const searchBar = document.querySelector('#search')
const searchBtn = document.querySelector('.btn')
const containerResult = document.querySelector('.container')

searchBtn.addEventListener('click', (e) => {
    query() 
})

document.addEventListener('keyup', (e) => {
    // if (e.code == "Enter")
        query()
})

function generateCard(data){
    let newCard = document.createElement('div')

    newCard.classList.add('card')

    let poster = document.createElement('img')
    let title = document.createElement('p')
    let score = document.createElement('span')

    poster.classList.add('poster')
    title.classList.add('title')
    score.classList.add('score')

    poster.setAttribute('src', data.show.image.original)
    title.textContent = data.show.name
    score.textContent = `Score: ${data.score.toFixed(2)}⭐`

    newCard.appendChild(poster)
    newCard.appendChild(title)
    newCard.appendChild(score)

    return newCard
}

function query(){
    let query = searchBar.value
    axios.get(`https://api.tvmaze.com/search/shows?q=${query}`).then((res) => {
        let { data } = res

        renderResults(data)
    })
}

function renderResults(results){
    containerResult.innerHTML = ""
    results.forEach((result) => {
        let newCard = generateCard(result)
        containerResult.appendChild(newCard)
    })
}