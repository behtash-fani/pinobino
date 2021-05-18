//create search board on top site for show result of searches
searchbar = document.getElementById("searchbar");
overlay = document.getElementById("overlay");
search_board = document.getElementById("search-board");

searchbar.addEventListener("click", function () {
    overlay.classList.add("overlay");
    search_board.style.display = "block";

});
overlay.addEventListener("click", function () {
    overlay.classList.remove("overlay");
    search_board.style.display = "none";

});
search_board.addEventListener("click", function () {
    overlay.classList.add("overlay");
})
overlay.addEventListener("click", function () {
    overlay.classList.remove("overlay");
})

//search engine
document.getElementById('searchbar').value = ''
const rdata = JSON.parse(data.replace(/&quot;/g, '"'))
const input = document.getElementById('searchbar')
const searchboard = document.getElementById('search-board')
let filteredArr = []

input.addEventListener('keyup', (e) => {
    searchboard.innerHTML = ''
    filteredArr = rdata.filter(pin => pin['caption'].includes(e.target.value))
    console.log(filteredArr)
    if (filteredArr.length > 0) {
        filteredArr.map(pin => {
            searchboard.innerHTML += `  <a href="http://127.0.0.1:8000/pin/${pin['slug']}">
                              <img class='thumbnail-bg m-2' width='10%' src="http://127.0.0.1:8000/media/${pin['image']}" />
                            </a>
                            <b> 
                              <a href="http://127.0.0.1:8000/pin/${pin['slug']}">
                                ${pin['caption']}
                              </a>  
                            </b>
                            <br>
                          `
        })
    } else {
        searchboard.innerHTML += '<b>No result founds...</b><br>'
    }
})
// another script
// tooltip jquery
$(document).ready(function () {
    $('[data-bs-toggle="tooltip"]').tooltip();
});
// script for follow and unfollow
