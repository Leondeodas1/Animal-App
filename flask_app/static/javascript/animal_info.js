var currentSearch = "";

function search(element){
    // console.log(element.value);
    currentSearch = element.value;
    console.log(currentSearch)
}













async function show() {
    var response = await fetch("https://api.api-ninjas.com/v1/animals?name=" + currentSearch + "/X-Api-Key=hFMh4udT9OaftkdG45PWuw==FsI9IWBQVHHxngSK");
    var coderData = await response.json(); 
    console.log(coderData)
    // thisis.innerHTML = makecodercard(coderData.current);
    // getid.innerHTML = forecastcard(coderData.forecast.forecastday[0]);
    // airquaity.innerHTML = airqua(coderData.current);
    // week.innerHTML = stevendayweathers(coderData.forecast.forecastday);
}