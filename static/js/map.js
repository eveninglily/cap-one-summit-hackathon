var map;
var purchaseMarker;
var altMarkers;

function initMap() {
    let dc = {lat: 38.9, lng: -77.01};
    map = new google.maps.Map(document.getElementById("map"), {
        center: dc,
        zoom: 14,
    });
}

function getSuggest(category, latlng) {
    $.getJSON('suggest', {'category': category, 'pos': latlng}, function(data) {
        let $recommendations = $("#recommendations > .collection");
        for (let i=0; i<data.length; i++) {
            $recommendations.append("<a class='collection-item merchant-item'><h5>"
                + data[i].name
                + "</h5></a>");
            altMarkers.push(new google.maps.Marker({
                position: {"lat": data[i].lat, "lng": data[i].lng},
                icon: "/uploads/alt_marker.png",
                map: map,
                title: data[i].name,
            }));
        }
    });
}

$(document).ready(function() {
    $("#purchase-history .purchase-item").click(function() {
        if (purchaseMarker) {
            purchaseMarker.setMap(null);
        }

        let geocodeStr = $(this).find("div.geocode").text();
        let commaPos = geocodeStr.indexOf(",");
        let latlng = {lat: parseFloat(geocodeStr.slice(0, commaPos)), lng: parseFloat(geocodeStr.slice(commaPos+1))};
        purchaseMarker = new google.maps.Marker({
            position: latlng,
            map: map,
        })

        map.panTo(latlng);

        if (altMarkers) {
            for (let i=0; i<altMarkers.length; i++) {
                altMarkers[i].setMap(null);
            }
        }

        altMarkers = [];
        $("#recommendations > .collection").empty();

        let category = $(this).find("div.category").text();
        if (category !== "other") {
            getSuggest(category, latlng);
        }
    });

    $("#recommendations .merchant-item").click(function() {
    });
});
