matches = require '../json/matches.json'

MAP_CENTER = [38.907, -77.0368]
MAP_ZOOM = 11 


$(document).ready -> 
    source = $('#popup-template').html()
    popupTemplate = Handlebars.compile(source)
    L.Icon.Default.imagePath = 'static/images'
    map = L.map('map').setView(MAP_CENTER, MAP_ZOOM)
    L.tileLayer(
        'http://{s}.tile.osm.org/{z}/{x}/{y}.png', 
        {attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'}
    ).addTo(map) 
    
    matchMarkers = L.layerGroup().addTo(map)
    matchMarkerPairs = []
    for match in matches
        lat = match[0]['lat']
        lng = match[0]['lon']
        m = L.marker([lat, lng], {icon: L.icon({iconUrl: 'static/images/shooting.png'})})
        popupValues = {
            OFFENSE: match[1].OFFENSE, 
            BLOCKSITEADDRESS: match[1].BLOCKSITEADDRESS,
            REPORTDATETIME: new Date(match[1].REPORTDATETIME['$date'])
        }
        m.bindPopup(L.popup({className: 'matchPopup'}).setContent(popupTemplate(match[1])))
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


 
    offenses = {}
    for [shot, crime] in matches
        if crime.OFFENSE of offenses
            offenses[crime.OFFENSE] += 1
        else
            offenses[crime.OFFENSE] = 1
    chart = c3.generate({
        bindto: '#offense-chart',
        data: {
            columns: [
                ['offenses'].concat(v for k, v of offenses)
            ],
            types: {
                offenses: 'bar',
            }
        },
        axis: {
            x: {
                type: 'category',
                categories: [k for k of offenses][0]
            },
            rotated: true
        }
    })

    crimes_in_range = []

    $('#slider').on('valuesChanging', (e, data) ->
        crimes_in_range = []
        for [match, marker] in matchMarkerPairs
            lat = match[0]['lat']
            lng = match[0]['lon']
            date = new Date(match[0].Date_Time)
            if date > data.values.min and date < data.values.max
                crimes_in_range.push(match[1])
                if not matchMarkers.hasLayer(marker)
                    matchMarkers.addLayer(marker)
            else
                matchMarkers.removeLayer(marker)
    )

    $('#slider').on('valuesChanged', (e, data) ->
        offenses = {}
        for crime in crimes_in_range
            if crime.OFFENSE of offenses
                offenses[crime.OFFENSE] += 1
            else
                offenses[crime.OFFENSE] = 1
        chart.load({
            columns: [['offenses'].concat(v for k, v of offenses)]
        }) 
    )
