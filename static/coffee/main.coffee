matches = require '../json/matches.json'

MAP_CENTER = [38.907, -77.0368]
MAP_ZOOM = 11
 
$(document).ready -> 
    # map = L.mapbox.map('map', 'examples.map-i86nkdio', {zoomControl: false})
    # heat = L.heatLayer(latlngs, {radius: 25}).addTo(map)

    map = L.map('map').setView(MAP_CENTER, MAP_ZOOM)
    L.tileLayer(
        'http://{s}.tile.osm.org/{z}/{x}/{y}.png', 
        {attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'}
    ).addTo(map);
    control = new L.Control.DateSlider().addTo(map);
    matchMarkers = L.layerGroup().addTo(map)
    date_start = new Date(2011, 1, 2, 11, 20)
    date_end = new Date(2013, 10, 24, 21, 55)
    $("#dateSlider").dateRangeSlider({
        bounds: {
            min: date_start,
            max: date_end
        },
        defaultValues: {
            min: date_start,
            max: date_end
        }
    })
    $('#dateSlider').on('valuesChanging', (e, data) ->
        for [match, marker] in matchMarkerPairs
            lat = match[0]['Latitude-100meter']
            lng = match[0]['Longitude-100meter']
            date = new Date(match[0]['Date_Time_UT'] * 1000)
            if date > data.values.min and date < data.values.max
                if not matchMarkers.hasLayer(marker)
                    matchMarkers.addLayer(marker)
            else
                matchMarkers.removeLayer(marker)   

    )

    matchMarkerPairs = []
    for match in matches
        lat = match[0]['Latitude-100meter']
        lng = match[0]['Longitude-100meter']
        m = L.marker([lat, lng])
        matchMarkers.addLayer(m)
        matchMarkerPairs.push([match, m])
