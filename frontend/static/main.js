//main.js

//Function to generate ranges and populate slectbox ////////
function generateOptions(start, end, increment) {
    var options = [];
    for (let i = start; i <= end; i += increment) {
        options.push(`<option value="${i}">${i}</option>`);
    }
    return options.join('');
}


function updateOptions () {
    var minPrice = parseInt(document.getElementById('minPriceRange').value, 10)
    var maxPrice = parseInt(document.getElementById('maxPriceRange').value, 10)

    // document.getElementById('maxPriceRange').innerHTML = generateOptions(5000,200000,5000)

    if (minPrice>=maxPrice) {
        newMaxPrice = minPrice+4000
        document.getElementById('maxPriceRange').value = newMaxPrice;
    } else {document.getElementById('maxPriceRange').value = maxPrice;}
}

document.getElementById('minPriceRange').innerHTML = generateOptions(1000, 195000, 5000)
document.getElementById('maxPriceRange').innerHTML = generateOptions(5000, 200000, 5000)

document.getElementById('minPriceRange').addEventListener('change', updateOptions)
document.getElementById('maxPriceRange').addEventListener('change', updateOptions)

document.getElementById('carSeats').innerHTML = generateOptions(2,8,2)


// Populates the text of the Min and Max price Value
document.getElementById('minPriceRange').addEventListener('input', function() {
    document.getElementById('minPriceRangeValue').textContent = this.value;});

document.getElementById('maxPriceRange').addEventListener('input', function() {
    document.getElementById('maxPriceRangeValue').textContent = this.value;});

// Populates Car Seat Value text
document.getElementById('carSeats').addEventListener('input', function() {
    document.getElementById('carSeatsValue').textContent = this.value;});

///////////////



// Hit Search button based on query options
function searchCars () {
    var query = document.getElementById('searchBar').value;
    var priceMin = document.getElementById('minPriceRange').value;
    var priceMax = document.getElementById('maxPriceRange').value;
    var carSeats = document.getElementById('carSeats').value;

    //Redirect to results after search is made
    window.location.href = "/results?query=" + query + "&minPrice=" + priceMin + "&maxPrice=" + priceMax + "&seats=" + carSeats;
}

// Navigate to teh about page
function about(){
    window.location.href = "/about"
}