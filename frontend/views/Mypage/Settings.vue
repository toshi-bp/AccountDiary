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
      <div>
        <h1>カテゴリーの追加</h1>
        <h3>収入か支出を選択してください</h3>
        <div>
          <el-select v-model="type" placeholder="Select">
            <el-option
              v-for="item in types"
              :key="item.id"
              :label="item.label"
              :value="item.value"
            />
          </el-select>
        </div>
        <div class="settings__input">
          <el-input v-model="newCategory"></el-input>
        </div>
        <div>
          <el-button @click="addCategory">
            カテゴリー追加
          </el-button>
        </div>
      </div>
    <!-- <h1>カテゴリー名の変更</h1>
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
    </div> -->
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
      newCategory: '',
      types: [{
        id: 1,
        value: 'income',
        label: '収入'
      }, {
        id: 2,
        value: 'expenditure',
        label: '支出'
      }],
    }
  },
  props: {
    userId: {
      type: String,
      default: localStorage.getItem('userId')
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
      axios.patch(
        '/api/categories/update',{}
      )
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
      // type→incomeとする
      axios.patch(
        '/api/users/update',
        {
          user_id: this.userId,
          money: this.money,
          type: 'income'
        }
      ).then(res => {
        console.log(res.data)
        console.log('money update is succeess!')
      }).catch(
        console.log('failed...')
      )
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
      axios.patch(
        '/api/users/update',
        {
          user_id: this.userId,
          password: this.password
        }
      ).then(res => {
        console.log(res.data)
        console.log('password update is succeess!')
      }).catch(
        console.log('failed...')
      )
    },
    addCategory() {
      const BASE_URL = "http://localhost:5000"
      let axios = Axios.create({
        baseURL: BASE_URL,
        headers: {
          'Content-type': 'application/json',
          'X-Requested-With': 'XMLHttpRequest'
        },
        responseType: 'json'
      })
      axios.post(
        '/api/categories/add',
        {
          user_id: this.userId,
          type: this.type,
          category: this.newCategory,
        }.then(res => {
          console.table(res.data)
        }).catch(
          console.log('failed...')
        )
      )
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
    await axios(`/api/categories/${this.userId}`).then(res => {
      console.log("user data")
      console.table(res.data)
      this.userCategories = res.data
    })
    this.saveUserId()
  }
}
</script>

<style lang="sass" scoped>
.settings
  $side-bar-width: 256px
  $main-width: calc(100% - #{$side-bar-width})
  &__main
    display: flex
    justify-content: center
    align-items: center
  &__input
    width: 200px
  &__button
    margin-bottom: 1rem
</style>