<template>
  <div class="analytics">
    <div>
      <side-bar
        :userId="this.userId"
        :money="userData.money"
        :used_money="userData.used_money"
      />
    </div>
    <div class="analytics__main">
      <h3>円グラフ</h3>
        <DoughnutChart :chartData="chartData" :options="options"/>
    </div>
  </div>
</template>

<script>
// コンポーネントをimportしない方針で進めてみる
// import ChartPie from '../../src/components/ChartPie.vue'
import { DoughnutChart } from 'vue-chart-3'
import { Chart, registerables } from 'chart.js'
import SideBar from '../../src/components/SideBar.vue'
import Axios from 'axios'
Chart.register(...registerables)

export default {
  data () {
    return {
      loading: false,
      chartData: null,
      userData: {},
      userHistory: [],
      labels: [],
      types: [],
      moneyData: [],
      colors: [],
      options: {
        responsive: true
      },
    }
  },
  components: {
    // ChartPie,
    SideBar,
    DoughnutChart,
  },
  props: {
    userId: {
      type: String,
      default: localStorage.getItem('userId')
    }
  },
  computed: {
    randomColor() {
      const color = (Math.random() * 0xFFFFFF | 0).toString(16)
      const randomColor = "#" + ("000000" + color).slice(-6);
      return randomColor
    }
  },
  methods: {
    saveUserId() {
      localStorage.setItem('userId', this.userId)
    },
  },
  mounted: async function() {
    const BASE_URL = "http://localhost:5000"
    let axios = Axios.create({
      baseURL: BASE_URL,
      headers: {
        'Content-type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest'
      },
      responseType: 'json'
    })
    // TODO:ユーザーデータ及び行動履歴データの取得
    await axios.get(`/api/users/${this.userId}`).then(res => {
      console.log("user data")
      console.table(res.data)
      this.userData = res.data
    })
    await axios.get(`/api/histories/${this.userId}`).then(res => {
      console.log("history data")
      console.table(res.data)
      const history = res.data
      // this.userHistory = res.data
      history.map((h) => {
        this.moneyData.push(h.result)
        this.labels.push(h.category)
        this.types.push(h.type)
        this.colors.push(this.randomColor)
      })
    })
    this.saveUserId()
    this.chartData = {
      labels: this.labels,
      datasets: [
        {
          data: this.moneyData,
          backgroundColor: this.colors
        }
      ],
    }
    console.log("chart data:", this.chartData)
    // labels→カテゴリ配分
    // moneyData→使ったお金の配分
  }
}
</script>

<style lang="sass" scoped>
.analytics
  $side-bar-width: 256px
  $main-width: calc(100% - #{$side-bar-width})
  &__main
    padding-left: $side-bar-width
</style>