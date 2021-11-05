<script>
  // import Chart from "chart.js";
  import { Pie } from "vue-chartjs";

  export default {
    extends: Pie,
    props: {
      chartData:{},
      options:{}
    },
    mounted() {
      if (this.chartData) {
        this.renderChart(this.chartData, this.options);
      }
    }
  }
</script>

