// startMap = $('#map-container')

let lat = 53;
let lng = 92;
//
// if (startMap[0].getAttribute('latitude').length !== 0) {
//     lat = startMap[0].getAttribute('latitude');
//     lng = startMap[0].getAttribute('longitude');
// }

let map = L.map('map-container').setView([lat, lng], 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

let markersGroup = L.layerGroup();
map.addLayer(markersGroup);

// L.marker([lat, lng]).addTo(markersGroup);

map.on('click', function (e) {
    markersGroup.clearLayers();

    let marker = L.marker(e.latlng).addTo(markersGroup);

    $('#id_latitude').val(marker.getLatLng()['lat'])
    $('#id_longitude').val(marker.getLatLng()['lng'])
});

allMaps = $('.map-place')

for (let i = 0; i < allMaps.length; i++) {
    let lat = allMaps[i].getAttribute('latitude')
    let lng = allMaps[i].getAttribute('longitude')

    let placeMap = L.map('map-' + (i + 1), {zoomControl: false, scrollWheelZoom: false}).setView([lat, lng], 13);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(placeMap);
    L.marker([lat, lng]).addTo(placeMap);
}


// showMap = $('.detailMap')
//
// let lat = showMap.getAttribute('latitude')
// let lng = showMap.getAttribute('longitude')
//
// let detailMap = L.map('detailMap').setView([lat, lng], 13);
//
// L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(detailMap);
// L.marker([lat, lng]).addTo(detailMap);
