var map;
function initMap() {
    let dc = {lat: 38.9, lng: -77.01};
    map = new google.maps.Map(document.getElementById("map"), {
        center: dc,
        zoom: 10
    });
}
