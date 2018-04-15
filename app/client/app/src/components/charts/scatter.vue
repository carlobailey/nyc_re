<template>
  <canvas v-bind:id="canvasId"></canvas>
</template>

<script>
import { watchData } from './base'
import Chart from 'chart.js'
export default {
  name: 'BarChart',
  props: ['chartData', 'canvasId'],
  mixins: [watchData],
  data () {
    return {
    }
  },
  mounted () {
    var ctx = document.getElementById(this.canvasId).getContext('2d')
    this.$chart = new Chart(ctx, {
      type: 'scatter',
      data: {
        datasets: this.chartData
      },
      options: {
        title: {
          display: true,
          text: 'This is temp'
        },
        scales: {
          xAxes: [{
            type: 'linear',
            position: 'bottom'
          }]
        }
      }
    })
  }
}
</script>

<style lang="sass" scoped>
</style>