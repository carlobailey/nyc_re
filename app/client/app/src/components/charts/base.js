import Vue from 'vue';
import Chart from 'chart.js'

Chart.defaults.global.maintainAspectRatio = false
Chart.defaults.global.legend.display = false
Chart.defaults.global.defaultFontSize = 11
// Chart.defaults.global.defaultFontFamily = 'Arial'

// Chart.defaults.global.animation.duration = 0
// Chart.defaults.global.hover.duration = 0
// Chart.defaults.global.responsiveAnimationDuration = 0

Chart.defaults.bar.scales.xAxes[0].gridLines.display = false
Chart.defaults.bar.scales.xAxes[0].gridLines.categoryPercentage = 0.5
Chart.defaults.bar.scales.xAxes[0].gridLines.barPercentage = 1.5

//https://github.com/chartjs/Chart.js/issues/4299
// Chart.defaults.global.defaultColor = ['#FFFF00']

var watchData = {
  watch: {
    chartLabels: function (newChartLabels) {
      this.$chart.data.labels = newChartLabels
      this.$chart.update()
    },
    chartData: function (newChartDataSet) {
      for (let i = 0; i < newChartDataSet.length; i++) {
          this.$chart.data.datasets[i].data = newChartDataSet[i].data
  				this.$chart.data.datasets[i].backgroundColor = newChartDataSet[i].backgroundColor
      }
  		this.$chart.update()
		}
  }
}

export { watchData }