L.Control.DateSlider = L.Control.extend({
    options: {
        position: 'bottomright'
    },

    onAdd: function (map) {
        this._map = map;
        
        var className = 'leaflet-control-button',
        container = L.DomUtil.create('div', className);
        container.id = "dateSlider";
            
        var title = L.DomUtil.create('div', 'date-slider-title', container);
        // $(title).html();
        
        // var today = new Date();
        // var lastWeek = new Date(today.getTime()-1000*60*60*24*7);
        // $(container).dateRangeSlider({
        //     bounds:{
        //         min: new Date(2013, 0, 1),
        //         max: today
        //     },
        //     defaultValues:{
        //         min: lastWeek,
        //         max: today
        //     }
        // });

        //You have to use $.proxy so we keep the right context in the handler methods
        $(container).on("mouseover",$.proxy(this._controlEnter, this));
        $(container).on("mouseout",$.proxy(this._controlLeave, this));
        
        return container;
    },

    onRemove: function (map) {
    },
    
    _controlEnter: function(e) {
        this._map.dragging.disable();
    },
    _controlLeave: function() {
        this._map.dragging.enable();
    }
});
