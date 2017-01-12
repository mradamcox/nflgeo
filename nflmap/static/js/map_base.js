var osm_attr = new ol.Attribution({
    html: '&copy; <a href="http://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a> contributors.'
});

var osm = {
    id: "osm",
    layer: new ol.layer.Tile({
        name: 'osm',
        source: new ol.source.XYZ({
            //url: 'https://a.tile.thunderforest.com/cycle/{z}/{x}/{y}.png',
            //url: 'https://{a-c}.tile.openstreetmap.org/{z}/{x}/{y}.png',
            // url: 'https://a.tile.thunderforest.com/spinal-map/{z}/{x}/{y}.png',
            url: 'http://{a-c}.tile.stamen.com/toner/{z}/{x}/{y}.png',
            // url: 'http://{a-c}.tile.stamen.com/watercolor/{z}/{x}/{y}.png',
            attributions: [osm_attr]
        }),
    })
};

var json = JSON.parse(document.getElementById("col_json").value);
console.log(json);

var pointsSource = new ol.source.GeoJSON({
    projection: 'EPSG:3857',
    object: json,
});

var stylew = new ol.style.Style({
    image: new ol.style.Circle({
        radius: 5,
        // stroke: new ol.style.Stroke({
            // color: 'red',
            // width: 2
        // }),
        fill: new ol.style.Fill({
            color: 'rgba(255,0,0,0.2)'
        })
    })
})

var styleg = new ol.style.Style({
    image: new ol.style.Circle({
        radius: 5,
        stroke: new ol.style.Stroke({
            color: 'red',
            width: 2
        }),
        // fill: new ol.style.Fill({
            // color: 'rgba(0,0,230,0.2)'
        // })
    })
})

var col = {
    id: "colleges",
    layer: new ol.layer.Vector({
        name: 'colleges',
        source: pointsSource,
        style: stylew,
    })
};

var collection = new ol.Collection([osm.layer,col.layer]);
$('#osm').addClass('selected');

var info_shown = false

var controls = [
    new ol.control.Zoom({
        zoomInTipLabel: 'zoom in',
        zoomOutTipLabel: 'zoom out'
    }),
    new ol.control.Attribution({
        tipLabel: 'layer attributions',
    })
];

var map = new ol.Map({
    target: 'map',
    renderer: 'canvas',
    layers: collection,
    controls: controls,
    view: new ol.View({
        center: ol.proj.transform([-97.3, 40], 'EPSG:4326', 'EPSG:3857'),
        maxZoom: 15,
        zoom: 4,
    }),
    minZoomLevel: 7,
});

function selectBasemap() {
    $('.bm').on('click', function() {
        $('.bm').removeClass('selected');
        $(this).addClass('selected');
        for(var i=0; i < basemaps.length; i++) {
            var basemap = basemaps[i]
            if (basemap.id === $(this).attr('id')) {
                collection.setAt(0, basemap.layer);
                
                break;
            }
        }
        map.setLayerGroup = new ol.layer.Group(collection);
    });
};

function selectOverlay() {
    $('.hm').on('click', function() {
        $('.hm').removeClass('selected');
        $(this).addClass('selected');
        for(var i=0; i < overlays.length; i++) {
            var overlay = overlays[i]
            if (overlay.id === $(this).attr('id')) {
                collection.setAt(1, overlay.layer);
                
                document.getElementById('layer-info').innerHTML = overlay.info
                break;
            }
        }
        map.setLayerGroup = new ol.layer.Group(collection);
    });
};

function tempRemoveOverlay() {
    var current_overlay = collection.getArray()[1];
    $('#temp-remove').on('mousedown', function() {
        current_overlay = collection.getArray()[1];
        collection.setAt(1, blank.layer);
        map.setLayerGroup = new ol.layer.Group(collection);
    });
    $('#temp-remove').on('mouseup', function() {
        collection.setAt(1, current_overlay);
        map.setLayerGroup = new ol.layer.Group(collection);
    });
};

function show_team() {
    $('.t-btn').on('click', function() {
        var code = this.id;
        $.ajax({
            url : '/json/'+code+'/',
            dataType : 'json',
            type : 'GET',
            success: function(data)
            {
                var new_layer = new ol.layer.Vector({
                    name: 'colleges',
                    source: new ol.source.GeoJSON({
                        projection: 'EPSG:3857',
                        object: data,
                    }),
                    style: styleg,
                });
                collection.setAt(2, new_layer);
                map.setLayerGroup = new ol.layer.Group(collection);
            }
        });
    });
}

$(document).ready(function() {
    document.getElementById('layer-info').innerHTML = "";
    tempRemoveOverlay();
    show_team();
}); 