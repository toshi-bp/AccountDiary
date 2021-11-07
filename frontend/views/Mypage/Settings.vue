<template>
<div>
  <div>
    <SideBar
      :money="userData.money"
      :used_money="userData.used_money"
    />
  </div>
  <div class="settings__main">
    <center>
    <h1>カテゴリー名の変更</h1>
    <p><h10>------変更前------</h10></p>
    <el-select v-model="category" placeholder="Select">
      <el-option
        v-for="item in userCategories"
        :key="item"
        :label="item.category"
        :value="item.category">
      </el-option>
    </el-select>
    <p><h10>------変更後------</h10></p>
    <div class="settings__input">
      <el-input v-model="changeCategory" placeholder="edit" />
    </div>
    <div class="settings__button">
      <el-button @click="sendChangeCategory">送信する</el-button>
    </div>
    <hr size="5" noshade="" color="#000">
    <h1>予算の設定</h1>
    <div class="settings__input">
      <el-input v-model="money" placeholder="edit" /> 円
    </div>
    <div class="settings__button">
      <el-button @click="setMoney">変更する</el-button>
    </div>
    <hr size="5" noshade="" color="#000" >
    <h1>個人情報</h1>
    <p><h10>------アカウント確認------</h10></p>
    <!--アカウント情報を掲載するテーブルの作成-->
    <p><h10>------パスワード変更------</h10></p>
    <div class="settings_input">
      <el-input v-model="password" placeholder="edit me" />
    </div>
    <div class="settings__button">
    <el-button @click="changePassword">送信する</el-button>
    </div>
    <hr size="5" noshade="" color="#000">
    </center>
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
      userData: {},
      userCategories: [],
      changeCategory: '',
      money: 0,
      password: '',
    }
  },
  props: {
    userId: {
      type: String
    }
  },
  methods: {
    saveUserId() {
      localStorage.setItem('userId', this.userId)
    },
    sendChangeCategory() {
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
    },
    setMoney() {
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
    },
    changePassword() {
      const BASE_URL = "http://localhost:5000"
      let axios = Axios.create({
        baseURL: BASE_URL,
        headers: {
          'Content-type': 'application/json',
          'X-Requested-With': 'XMLHttpRequest'
        },
        responseType: 'json'
      })
      // パスワードの更新
      console.log(axios)
    }
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
    // ユーザーデータの取得
    await axios.get(`/api/users/${this.userId}`).then(res => {
      console.log("user data")
      console.table(res.data)
      this.userData = res.data
    })
    // カテゴリーの取得
    await axios.get(`/api/categories/${this.userId}`).then(res => {
      console.log("user data")
      console.table(res.data)
      this.userCategories = res.data
    })
    this.saveUserId()
  }
}
</script>

<style lang="sass" scoped>
.mypage
  $side-bar-width: 256px
  $main-width: calc(100% - #{$side-bar-width})
  &__header
    padding-left: $side-bar-width
  &__side
    display: block
  &__main
    margin-top: 2rem
    width: $main-width
    padding-left: $side-bar-width
    display: block
  &__img-container
    display: block
    margin: 0 auto
  &__img
    display: flex
    flex-wrap: wrap
    &__body
      display: block
      border: 1px solid #000
      width: 200px
      margin: 0 0.5rem 1rem
.el-input
  width: 200px
  margin-bottom: 1rem
.settings
  $side-bar-width: 256px
  $main-width: calc(100% - #{$side-bar-width})
  &__main
    display: flex
    justify-content: center
    align-items: center
  &__button
    margin-bottom: 1rem

</style>