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
      <chart-pie
        :labels="labels"
        :moneyData="moneyData"
        :colors="colors"
      />
    </div>
  </div>
</template>

<script>
import ChartPie from '../../src/components/ChartPie.vue'
import SideBar from '../../src/components/SideBar.vue'
import Axios from 'axios'

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
    }
  },
  components: {
    ChartPie,
    SideBar,
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
      const userHistory = res.data
      // this.userHistory = res.data
      userHistory.map((history) => {
        this.moneyData.push(history.result)
        this.labels.push(history.category)
        this.types.push(history.type)
        this.colors.push(this.randomColor)
      })
    })
    this.saveUserId()
    console.log("money data:", this.moneyData)
    console.log("labels:", this.labels)
    console.log("types:", this.types)
    console.log("colors", this.colors)
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