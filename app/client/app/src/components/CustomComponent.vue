<template>
  <section style="height=100%">

    <div class="card">
      <header class="card-header">
          <div>
            <div class="dropdown"
              v-bind:class="{ 'is-active': isActive2 }"
              v-on:click="isActive2 = !isActive2">
              <div class="dropdown-trigger">
                <button class="button smallFont is-small" aria-haspopup="true" aria-controls="dropdown-menu">
                  <span>Level of detail</span>
                  <span class="icon is-small">
                    <i class="fas fa-angle-down" aria-hidden="true"></i>
                  </span>
                </button>
              </div>
              <div class="dropdown-menu" id="dropdown-menu" role="menu">
                <div class="dropdown-content" style="max-height: 200px; overflow-y: scroll;">
                    <a v-for="item in LoD" :key="item" class="dropdown-item"
                    @click="selectedDetail=item">
                      {{ item }}
                    </a>
                </div>
              </div>
            </div>
          </div>
          <div>
            <div class="dropdown"
              v-bind:class="{ 'is-active': isActive }"
              v-on:click="isActive = !isActive">
              <div class="dropdown-trigger">
                <button class="button smallFont is-small" aria-haspopup="true" aria-controls="dropdown-menu">
                  <span>Select Dataset</span>
                  <span class="icon is-small">
                    <i class="fas fa-angle-down" aria-hidden="true"></i>
                  </span>
                </button>
              </div>
              <div class="dropdown-menu" id="dropdown-menu" role="menu">
                <div class="dropdown-content" style="max-height: 200px; overflow-y: scroll;">
                    <a v-for="item in columns" :key="item" class="dropdown-item" @click="fetchGeoLayers({'type': selectedDetail, 'column': item})">
                      {{ item }}
                    </a>
                </div>
              </div>
            </div>
        </div>
      </header>
      <div class="card-content">
        <div class="content">
          <div class="columns">
            <div class="column is-9">
              <div id="mapid" class="map"></div>
            </div>
            <div class="column is-3" v-if="legendLabels !== null">
              <div id="legendContainer" class="card">
                <div class="card-header" style="background-color: black;">
                  <strong style="color: white;">{{ selectedData }}</strong>
                </div>
                <div class="card-content">
                  <div class="content">
                    <div v-for="thing in legendLabels" :key="thing.color">
                      <div class="valueBox" v-bind:style="{ 'background-color': thing.color }"></div>
                        <span class="legendFont">{{ thing.label }}</span>
                      </div>
                    <div class="box">
                      <div class="">
                        <corr-scatter :canvasId="'corr-scatter'"
                                    :chartData="corrData">
                                    </corr-scatter>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

  </section>
</template>

<script>

import backend from '../store/backend'
import 'leaflet'
import scatter from '../components/charts/scatter'

const L = window.L

export default {
  name: 'CustomComponent',
  components: {
    'corr-scatter': scatter
  },
  data () {
    return {
      // FiX this
      isActive: false,
      isActive2: false,
      map: null,
      tileLayer: null,
      geojson: null,
      columns: [],
      selectedData: null,
      legendLabels: null,
      LoD: ['zip', 'coordinates'],
      selectedDetail: null,
      corrData: [{
        label: 'Actual Revenue',
        data: [{
          x: 0.1,
          y: 0.3
        }, {
          x: 0.5,
          y: 0.2
        }, {
          x: 0.6,
          y: 0.9
        }, {
          x: 0.1,
          y: 0.1
        }, {
          x: 0.10,
          y: 0.10
        }, {
          x: 0.9,
          y: 0.7
        }, {
          x: 0.4,
          y: 0.5
        }],
        borderColor: '#7FAACC',
        backgroundColor: '#7FAACC'
      }]
    }
  },
  watch: {
    selectedDetail: function (newValue) {
      let self = this
      backend.fetchColumnNames(newValue, function (respData) {
        self.columns = respData
      })
    }
  },
  methods: {
    legendMaker (colorList) {
    },
    fetchColumnNames (input) {
      var self = this
      backend.fetchColumnNames(input, function (respData) {
        var val = respData
        self.columns = val
      })
    },
    initMap () {
      // TO DO: optimize with vectorgrid
      this.map = L.map('mapid', {
        preferCanvas: true,
        minZoom: 2,
        maxZoom: 16}).setView([40.7128, -74.0060], 12)
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
      this.selectedData = inputs.column
      var self = this
      backend.fetchGeoLayers(inputs, function (respData) {
        var geo = respData
        // console.log(geo.features)
        var values = geo.features.map(function (i) { return i.properties[inputs.column] })
        var min = Math.min(...values)
        var max = Math.max(...values)
        var valueRanges = []
        var incmt = Math.ceil((max - min) / 7)
        for (var i = min; i <= max; i++) {
          if (i && (i % incmt === 0)) {
            valueRanges.push(i)
          }
        }
        function getColor (d) {
          return d > valueRanges[5] ? '#800026'
            : d > valueRanges[4] ? '#BD0026'
              : d > valueRanges[3] ? '#E31A1C'
                : d > valueRanges[2] ? '#FC4E2A'
                  : d > valueRanges[1] ? '#FD8D3C'
                    : d > valueRanges[0] ? '#FEB24C'
                      : d > 0 ? '#FED976'
                        : '#FFEDA0'
        }
        function style (feature) {
          return {
            fillColor: getColor(feature.properties[inputs.column], valueRanges),
            weight: 0.75,
            opacity: 1,
            color: 'white',
            fillOpacity: 0.7
          }
        }
        self.map.eachLayer(function (layer) {
          if (layer !== self.tileLayer) {
            self.map.removeLayer(layer)
          }
        })
        // var test
        if (inputs.type === 'coordinates') {
          L.geoJSON(geo, {
            pointToLayer: function (feature, latlng) {
              return new L.CircleMarker(latlng, {
                radius: 8,
                fillOpacity: 0.4,
                color: 'white',
                fillColor: getColor(feature.properties[inputs.column]),
                weight: 1})
            }
          }).addTo(self.map)
        } else {
          self.geojson = L.geoJSON(geo, {style: style})
          self.geojson.addTo(self.map)
        }
        var colorList = ['#FFEDA0', '#FED976', '#FEB24C', '#FD8D3C', '#FC4E2A', '#E31A1C', '#BD0026', '#800026']
        var grades = valueRanges
        // TO DO: fix last item in legend
        grades.unshift(0)
        // FIX THIS: temp solution to have dynamic legend
        self.legendLabels = []
        for (var j = 0; j < grades.length - 1; j++) {
          if (grades[j + 1] === undefined) {
            self.legendLabels.push({'color': colorList[j], 'label': grades[j] + ' +'})
          }
          self.legendLabels.push({'color': colorList[j], 'label': grades[j] + ' -- ' + grades[j + 1]})
        }
      })
    }
  },
  computed: {
    resource () {
      // To display `resourceOne` value from the backend
      return this.$store.state.resource
    }
  },
  mounted () {
    this.initMap()
    this.initLayers()
    // this.fetchGeoLayers({'type': 'coordinates', 'column': 'total_parks'})
  },
  created () {
    // this.fetchColumnNames({'detail': 'zip'})
  }
}
</script>

<style lang="sass" scoped>
.card-content {padding: 0.5em;}
.card-header {border-color: white !important; box-shadow: none; padding: 0.4em;}
.valueBox {display: inline-block; height: 20px !important; width: 20px !important; opacity: 0.75; border-radius: 0px; box-shadow: none; margin-bottom: 2px !important;}
.button {border-radius: 0px !important;}
.legend {line-height: 18px; color: #555; }
.legend i {width: 18px; height: 18px; float: left; margin-right: 8px; opacity: 0.7; }
.box {border-radius: 0px;}

</style>
