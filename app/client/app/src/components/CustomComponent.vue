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
          <div>{{ test }}</div>
          <div id="mapid">
            <v-map :zoom=13 :center="[40.7128, -74.0060]">
              <v-tilelayer url="https://server.arcgisonline.com/arcgis/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}"></v-tilelayer>
              <!-- <v-marker :lat-lng="[40.7128, -74.0060]"></v-marker> -->
              <v-polygon :lat-lngs="[
                                  [51.509, -0.08],
                                  [51.503, -0.06],
                                  [51.51, -0.047]]"></v-polygon>
            </v-map>
          </div>
        </div>
      </div>
    </div>

  </section>
</template>

<script>

import backend from '../store/backend'
import Vue2Leaflet from 'vue2-leaflet'

export default {
  name: 'CustomComponent',
  components: {
    'v-map': Vue2Leaflet.Map,
    'v-tilelayer': Vue2Leaflet.TileLayer,
    'v-marker': Vue2Leaflet.Marker,
    'v-polygon': Vue2Leaflet.Polygon
  },
  data () {
    return {
      test: null
    }
  },
  watch: {
    viewToggleOther (bool) {
      this.setToggle('other', bool)
    }
  },
  methods: {
    setToggle: function (name, bool) {
      console.log('Toggle Called')
      // this.$store.commit('setToggle', [name, bool])
    },
    fetchTest () {
      var self = this
      backend.fetchTestingTesty(function (respData) {
        var val = respData
        self.test = val
        console.log(respData)
      })
    },
    fetchGeoLayers (inputs) {
      console.log(inputs)
      backend.fetchGeoLayers(inputs, function (respData) {
        var val = respData
        // self.test = val
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
  mounted () {
    this.$store.dispatch('fetchResourceOne')
    this.fetchTest()
    this.fetchGeoLayers('zip')
  }
}
</script>

<style lang="sass" scoped>
#mapid { height: 380px; }
@import "../../node_modules/leaflet/dist/leaflet.css"

</style>
