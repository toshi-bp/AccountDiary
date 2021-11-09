<script>
import { Chart, registerables } from 'chart.js'
import { DoughnutChart } from 'vue-chart-3'
Chart.register(...registerables)
export default {
  data () {
    return {
      options: {
        responsive: true
      },
      chartData: {},
    }
  },
  components: {
    DoughnutChart
  },
  props: {
    labels: [],
    moneyData: [],
    colors: [],
  },
  async mounted () {
    this.chartData = {
      labels: this.labels,
      dataSets: [
        {
          label: "円グラフ",
          data: this.moneyData,
          backgroundColor: this.colors
        }
      ],
      hoverOffset: 4
    }
    console.log("chart data")
    console.table(this.chartData)
    await this.renderChart(this.chartData, this.options)
  },
}
</script>
