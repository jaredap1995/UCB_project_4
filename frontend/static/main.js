//main.js

//Helper Functions: 

// Function to generate ranges and populate selectbox for nums
function generateOptions(start, end, increment) {
    var options = [];
    for (let i = start; i <= end; i += increment) {
        options.push(`<option value="${i}">${i}</option>`);
    }
    options.reverse()
    return options.join('');
}

// Same function but for string values
function generateStringOptions (array) {
    var options=[]
    for (let choice of array) {
        options.push(`<option value= "${choice}">${choice}</option>`)
    }
    return options.join('')
}


///////////////////////////////////////



// Populating initial values
document.getElementById('maxPriceRange').innerHTML = generateOptions(5000, 200000, 5000)

let conditionsArray = ['any','good', 'excellent', 'fair', 'like new', 'new', 'salvage']
let newConditionsArray = conditionsArray.map(function(x) { return x.charAt(0).toUpperCase() + x.slice(1,)})
document.getElementById('condition').innerHTML = generateStringOptions(newConditionsArray)


let stateArray = ['any','az', 'ar', 'fl', 'ma', 'nc', 'ny', 'or', 'pa', 'tx', 'wa', 'wi',
'al', 'ak', 'ca', 'co', 'ct', 'dc', 'de', 'ga', 'hi', 'id', 'il',
'in', 'ia', 'ks', 'ky', 'la', 'me', 'md', 'mi', 'mn', 'ms', 'mo',
'mt', 'ne', 'nv', 'nj', 'nm', 'nh', 'nd', 'oh', 'ok', 'ri', 'sc',
'sd', 'tn', 'ut', 'vt', 'va', 'wv', 'wy']
let newStateArray = stateArray.map(function(x){return x.toUpperCase()})
document.getElementById('state').innerHTML=generateStringOptions(newStateArray)


let brandArray = ['any', 'gmc', 'chevrolet', 'toyota', 'ford', 'jeep', 'nissan', 'ram',
'mazda', 'cadillac', 'honda', 'dodge', 'lexus', 'jaguar', 'buick',
'chrysler', 'volvo', 'audi', 'infiniti', 'lincoln', 'alfa-romeo',
'subaru', 'acura', 'hyundai', 'mercedes-benz', 'bmw', 'mitsubishi',
'volkswagen', 'porsche', 'kia', 'rover', 'ferrari', 'mini',
'pontiac', 'fiat', 'tesla', 'saturn', 'mercury', 'harley-davidson',
'datsun', 'aston-martin', 'land rover', 'morgan']
let newBrands = brandArray.map(function(x) { return x.charAt(0).toUpperCase() + x.slice(1,)})
document.getElementById('manufacturer').innerHTML = generateStringOptions(newBrands)

let size = ['any', 'full-size', 'mid-size', 'compact', 'sub-compact']
let newSize = size.map(function(x) { return x.charAt(0).toUpperCase() + x.slice(1,)})
document.getElementById('size').innerHTML = generateStringOptions(newSize)

let transmissionArray = ['any', 'other', 'automatic', 'manual']
let newTransmissionArray = transmissionArray.map(function(x) {return x.charAt(0).toUpperCase() + x.slice(1,)})
document.getElementById('transmission').innerHTML = generateStringOptions(newTransmissionArray)

// Populates the text Value upon change
// document.getElementById('maxPriceRange').addEventListener('input', function() {
//     document.getElementById('maxPriceRangeValue').textContent = this.value;});

///////////////



// Hit Search button based on query options
function searchCars () {
    var query = document.getElementById('searchBar').value;
    var priceMax = document.getElementById('maxPriceRange').value;
    var carSeats = document.getElementById('carSeats').value;

    //Redirect to results after search is made
    window.location.href = "/results?query=" + query + "&minPrice=" + priceMin + "&maxPrice=" + priceMax + "&seats=" + carSeats;
}

// Navigate to teh about page
function about(){
    window.location.href = "/about"
}