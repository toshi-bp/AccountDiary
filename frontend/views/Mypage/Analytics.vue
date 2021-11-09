<template>
  <div class="analytics">
    <div>
      <side-bar
        :userId="this.userId"
      />
    </div>
    <div>
      <h3>円グラフ</h3>
      <chart-pie
        :chartData="hoge"
        :options="huga"
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
    }
  },
  components: {
    ChartPie,
    SideBar,
  },
  props: {
    userId: {
      type: String,
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
    console.log(axios)
    // TODO:ユーザーデータ及び行動履歴データの取得
    axios.get()
  }
}
</script>

<style lang="sass" scoped>

</style>