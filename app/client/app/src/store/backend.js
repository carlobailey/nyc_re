import axios from 'axios'


let $backend = axios.create({
    baseURL: 'http://127.0.0.1:5000/api/',
    timeout: 7500,
    headers: {'Content-Type': 'application/json'}
})

$backend.interceptors.response.use(function (response) {
    return response
  }, function (error) {
    console.log(error)
    return Promise.reject(error)
  });

export default {

  fetchResourceOne () {
    return $backend.get(`resource/one`)
      .then(response => response.data)
  },

  fetchResourceTwo (resourceId) {
    return $backend.get(`resource/two/${resourceId}`)
      .then(response => response.data)
  },

  fetchTestingTesty (callback) {
    console.log('made it to this point')
    $backend.get(`testing/testy`)
      .then(response => {
        console.log('got to the end of backend request')
        return callback(response.data)
      })
    },

  fetchGeoLayers (input, callback) {
    console.log('Fetching Geo Layers')
    $backend.get(`/geodata/layers/zip`)
      .then(response => {
        console.log('Got Geo Layers')
        return callback(response.data)
      })
    }
}