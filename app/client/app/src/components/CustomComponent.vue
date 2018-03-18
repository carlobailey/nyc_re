<template>
  <section>

    <div class="card">
      <header class="card-header">
        <p class="card-header-title">
          Testing Page One
        </p>
      </header>
      <div class="card-content">
        <div class="content">
          Content
          <div>{{ resource }}</div>
        </div>
      </div>

      <div class="card-content">
        <div class="content">
          Test Location
          <!-- <div>{{ test }}</div> -->
          <!-- <div id="mapid">
            <v-map :zoom=13 :center="[40.7128, -74.0060]" ref="map">
              <v-tilelayer url="https://server.arcgisonline.com/arcgis/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}"></v-tilelayer>
              <v-polygon :lat-lngs="[
                                  [51.509, -0.08],
                                  [51.503, -0.06],
                                  [51.51, -0.047]]"></v-polygon>
              <v-geojson :geojson="geojson" ref="geo"></v-geojson> 
            </v-map>
          </div> -->
          <div id="mapid" class="map"></div>
        </div>
      </div>
    </div>

  </section>
</template>

<script>

import backend from '../store/backend'
import Vue2Leaflet from 'vue2-leaflet'
import 'leaflet'

const L = window.L

export default {
  name: 'CustomComponent',
  components: {
    'v-map': Vue2Leaflet.Map,
    'v-tilelayer': Vue2Leaflet.TileLayer,
    'v-marker': Vue2Leaflet.Marker,
    'v-polygon': Vue2Leaflet.Polygon,
    'v-geojson': Vue2Leaflet.GeoJSON
  },
  data () {
    return {
      map: null,
      tileLayer: null,
      geojson: null,
      layers: []
    }
  },
  methods: {
    initMap () {
      this.map = L.map('mapid').setView([40.7128, -74.0060], 12)
      this.tileLayer = L.tileLayer('https://server.arcgisonline.com/arcgis/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}')
      this.tileLayer.addTo(this.map)
    },
    initLayers () {},
    setToggle: function (name, bool) {
      // console.log('Toggle Called')
      // this.$store.commit('setToggle', [name, bool])
    },
    fetchTest () {
      var self = this
      backend.fetchTestingTesty(function (respData) {
        var val = respData
        self.test = val
      })
    },
    fetchGeoLayers (inputs) {
      console.log('leaf works')
      console.log(L)
      var self = this
      backend.fetchGeoLayers(inputs, function (respData) {
        var geo = respData
        var values = geo.features.map(function (i) { return i.properties.total_parks })
        var min = Math.min(...values)
        var max = Math.max(...values)
        var valueRanges = []
        var incmt = Math.ceil((max - min) / 7)
        for (var i = min; i <= max; i++) {
          if (i && (i % incmt === 0)) {
            valueRanges.push(i)
          }
        }
        function getColor (d, arr) {
          return d > arr[5] ? '#800026'
            : d > arr[4] ? '#BD0026'
              : d > arr[3] ? '#E31A1C'
                : d > arr[2] ? '#FC4E2A'
                  : d > arr[1] ? '#FD8D3C'
                    : d > arr[0] ? '#FEB24C'
                      : d > 0 ? '#FED976'
                        : '#FFEDA0'
        }
        function style (feature) {
          return {
            fillColor: getColor(feature.properties.total_parks, valueRanges),
            weight: 0.75,
            opacity: 1,
            color: 'white',
            fillOpacity: 0.7
          }
        }
        self.geojson = L.geoJSON(geo, {style: style})
        self.geojson.addTo(self.map)
      })
      // console.log(this.$refs.geo)
    },
    fetchStyling () {
      var self = this
      backend.fetchStyling(function (respData) {
        var val = respData
        self.options = val
        console.log(val)
      })
    }
  },
  computed: {
    resource () {
      // To display `resourceOne` value from the backend
      return this.$store.state.resource
    }
  },
  watch: {
    options: function () {
      let self = this
      backend.fetchStyling(function (respData) {
        var val = respData
        self.options = val
        console.log(val)
      })
    }
  },
  mounted () {
    this.initMap()
    this.initLayers()
    this.fetchGeoLayers({'type': 'zip', 'column': 'total_parks'})
  }
}
</script>

<style lang="sass" scoped>
#mapid { height: 500px; }

</style>
