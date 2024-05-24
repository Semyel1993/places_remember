function formCreate() {
    //Krasnoyarsk
    let lat = 56.0184;
    let lng = 92.8672;

    let mapFormCreate = L.map('map-form-create').setView([lat, lng], 10);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(mapFormCreate);


    let markersGroup = L.layerGroup();
    mapFormCreate.addLayer(markersGroup);


    mapFormCreate.on('click', function (e) {
        markersGroup.clearLayers();

        let marker = L.marker(e.latlng).addTo(markersGroup);

        $('#id_latitude').val(marker.getLatLng()['lat'])
        $('#id_longitude').val(marker.getLatLng()['lng'])
    });
}


let allPlaceMaps = $('.map-place')

for (let i = 0; i < allPlaceMaps.length; i++) {
    let lat = allPlaceMaps[i].getAttribute('latitude')
    let lng = allPlaceMaps[i].getAttribute('longitude')

    let placeMap = L.map('map-' + (i + 1), {zoomControl: false, scrollWheelZoom: false}).setView([lat, lng], 10);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(placeMap);
    L.marker([lat, lng]).addTo(placeMap);
}


let currentCoordinates = $('#detailMap')

let placeLat = currentCoordinates[0].getAttribute('latitude')
let placeLng = currentCoordinates[0].getAttribute('longitude')

let mapCurrentPlace = L.map('detailMap').setView([placeLat, placeLng], 10);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(mapCurrentPlace);
L.marker([placeLat, placeLng]).addTo(mapCurrentPlace);


function formEdit() {
    let mapEditCurrentPlace = L.map('map-form-edit').setView([placeLat, placeLng], 10);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(mapEditCurrentPlace);


    let markersGroup = L.layerGroup();
    mapEditCurrentPlace.addLayer(markersGroup);
    L.marker([placeLat, placeLng]).addTo(markersGroup);


    mapEditCurrentPlace.on('click', function (e) {
        markersGroup.clearLayers();

        let marker = L.marker(e.latlng).addTo(markersGroup);

        $('#id_latitude').val(marker.getLatLng()['lat'])
        $('#id_longitude').val(marker.getLatLng()['lng'])
    });
}
