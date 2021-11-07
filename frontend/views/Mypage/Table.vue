<template>

<div>
  <div>
    <sideBar
      :userId="this.userId"
      :used_money="userData.used_money"
      :money="userData.money"
    />
  </div>
  <div class="table__main">
    <div class="table__center">
      <el-table
        :data="userHistory"
        max-height="1000">
        <el-table-column
          prop="act_time"
          label="日付"
          width="100">
        </el-table-column>
        <el-table-column
          prop="category"
          label="カテゴリ"
          width="120">
        </el-table-column>
        <el-table-column
          prop="result"
          label="金額"
          width="120">
        </el-table-column>
        <el-table-column
          prop="place"
          label="場所"
          width="120">
        </el-table-column>
        <!-- <el-table-column
          prop="photo"
          label="写真"
          width="180">
        </el-table-column> -->
        <el-table-column
          label="Operations"
          width="120">
          <template v-slot="scope">
            <el-button
              @prevent="deleteRow(scope.$index, tableData)"
              type="text"
              size="small">
              編集
            </el-button>
          </template>
        </el-table-column>
        </el-table>
      </div>
  </div>
</div>

</template>

<script>
import SideBar from '../../src/components/SideBar.vue'
import Axios from 'axios'


export default {
  components:{
  SideBar,
  },
  data() {
    return {
      userHistory: [],
      userData: {},
    }
  },
  props: {
    userId: {
      type: String,
      default: localStorage.getItem('userId')
    },
  },
  methods: {
    saveUserId() {
      localStorage.setItem('userId', this.userId)
    }
  },
  mounted: async function () {
    console.log("user id:" + this.userId)
    const BASE_URL = "http://localhost:5000"
    let axios = Axios.create({
      baseURL: BASE_URL,
      headers: {
        'Content-type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest'
      },
      responseType: 'json'
    })
    await axios.get(
      `/api/users/${this.userId}`).then(res => {
      console.log("user data")
      console.table(res.data)
      this.userData = res.data
    })
    await axios.get(
      `/api/histories/${this.userId}`).then(res => {
      console.log("history data")
      console.table(res.data)
      this.userHistory = res.data
    })
    this.saveUserId()
  }
}
</script>

<style lang="sass" scoped>
.table
  $side-bar-width: 256px
  $main-width: calc(100% - #{$side-bar-width})
  &__main
    margin-top: 2rem
    width: $main-width
    padding-left: $side-bar-width
    display: block
  &__center
    margin: 0 auto
  /* // .el-row
  //   margin-bottom: 20px
  //   &:last-child
  //     margin-bottom: 0rem
  // .el-col
  //   border-radius: 4px */
</style>