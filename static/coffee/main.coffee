matches = require '../json/matches.json'

MAP_CENTER = [38.907, -77.0368]
MAP_ZOOM = 11
$(document).ready -> 
    L.Icon.Default.imagePath = 'static/images'
    map = L.map('map').setView(MAP_CENTER, MAP_ZOOM)
    L.tileLayer(
        'http://{s}.tile.osm.org/{z}/{x}/{y}.png', 
        {attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'}
    ).addTo(map) 
    
    matchMarkers = L.layerGroup().addTo(map)
    matchMarkerPairs = []
    for match in matches
        lat = match[0]['Latitude-100meter']
        lng = match[0]['Longitude-100meter']
        m = L.marker([lat, lng], {icon: L.icon({iconUrl: 'static/images/shooting.png'})})
        m.bindPopup(L.popup({className: 'matchPopup'}).setContent('foobar'))
        matchMarkers.addLayer(m)
        matchMarkerPairs.push([match, m])

    date_start = new Date(2011, 1, 2, 11, 20)
    date_end = new Date(2013, 6, 22, 21, 55)
    $("#slider").dateRangeSlider({
        bounds: {
            min: date_start,
            max: date_end
        },
        defaultValues: {
            min: date_start,
            max: date_end
        }
    })

    $('#slider').on('valuesChanging', (e, data) ->
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

