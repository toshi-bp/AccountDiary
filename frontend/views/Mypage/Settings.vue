<template>
  <div>
    <div>
      <SideBar
        :userId="this.userId"
        :money="userData.money"
        :used_money="userData.used_money"
      />
    </div>
    <div class="settings__main">
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
      <h1>予算の設定</h1>
      <div class="settings__input">
        <el-input v-model="money" placeholder="edit">
          <template #append>円</template>
        </el-input>
      </div>
      <div class="settings__button">
        <el-button @click="setMoney">変更する</el-button>
      </div>
      <h1>個人情報</h1>
      <p>------アカウント確認------</p>
      <!--アカウント情報を掲載するテーブルの作成-->
      <table class="settings__table">
        <tbody>
          <tr>
            <td>ユーザー名</td>
            <td>{{ userData.name }}</td>
          </tr>
          <tr>
            <td>メールアドレス</td>
            <td>{{ userData.mail }}</td>
          </tr>
          <tr>
            <td>生年月日</td>
            <td>{{ userData.birthday }}</td>
          </tr>
          <tr>
            <td>性別</td>
            <td>{{ showGender }}</td>
          </tr>
          <tr>
            <td>電話番号</td>
            <td>{{ userData.phonenumber }}</td>
          </tr>
        </tbody>
      </table>
      <p>------パスワード変更------</p>
      <div class="settings_input">
        <el-input v-model="password" placeholder="edit me" />
      </div>
      <div class="settings__button">
        <el-button @click="changePassword">パスワード変更</el-button>
      </div>
    </div>
  </div>
</template>


<script>
import SideBar from '../../src/components/SideBar.vue'
import Axios from 'axios'
import crypto from 'crypto'

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
      type: '',
      types: [{
        id: 1,
        value: 'income',
        label: '収入'
      }, {
        id: 2,
        value: 'expenditure',
        label: '支出'
      }],
      addBudget: 'income',
    }
  },
  props: {
    userId: {
      type: String,
      default: localStorage.getItem('userId')
    }
  },
  computed: {
    showGender() {
      if (this.userData.gender === "male") {
        return "男"
      } else if (this.userData.gender === "female") {
        return "女"
      } else {
        return "その他"
      }
    }
  },
  methods: {
    saveUserId() {
      localStorage.setItem('userId', this.userId)
    },
    async setMoney() {
      const BASE_URL = 'https://nikkidekakeibo.herokuapp.com'
      // const BASE_URL = "http://localhost:5000"
      let axios = Axios.create({
        baseURL: BASE_URL,
        headers: {
          'Content-type': 'application/json',
          'X-Requested-With': 'XMLHttpRequest'
        },
        responseType: 'json'
      })
      let self = this
      // type→incomeとする
      await axios.patch(
        `/api/users/update_money/${self.userId}`,
        {
          user_id: self.userId,
          money: Number(self.money),
          type: self.addBudget,
        }
      ).then(res => {
        console.log(res.data)
        console.log('money update is succeess!')
      })
    },
    async changePassword() {
      // const BASE_URL = "http://localhost:5000"
      const BASE_URL = 'https://nikkidekakeibo.herokuapp.com'
      let axios = Axios.create({
        baseURL: BASE_URL,
        headers: {
          'Content-type': 'application/json',
          'X-Requested-With': 'XMLHttpRequest'
        },
        responseType: 'json'
      })
      // パスワードの更新
      let sha256 = crypto.createHash('sha256')
      sha256.update(this.password)
      const hashPass = sha256.digest('base64')
      let self = this
      await axios.patch(
        `/api/users/update_pass/${self.userId}`,
        {
          user_id: self.userId,
          password: hashPass
        }
      ).then(res => {
        console.log(res.data)
        console.log('password update is succeess!')
      }).catch(
        console.log('failed...')
      )
    },
    addCategory() {
      // const BASE_URL = "http://localhost:5000"
      const BASE_URL = 'https://nikkidekakeibo.herokuapp.com'
      let axios = Axios.create({
        baseURL: BASE_URL,
        headers: {
          'Content-type': 'application/json',
          'X-Requested-With': 'XMLHttpRequest'
        },
        responseType: 'json'
      })
      let self = this
      axios.post(
        '/api/categories/add',
        {
          user_id: self.userId,
          type: self.type,
          category: self.newCategory,
        }
      ).then(res => {
        console.table(res.data)
      }).catch(
        console.log('category add failed...')
      )
    }
  },
  mounted: async function() {
    // const BASE_URL = "http://localhost:5000"
    const BASE_URL = 'https://nikkidekakeibo.herokuapp.com'
    let axios = Axios.create({
      baseURL: BASE_URL,
      headers: {
        'Content-type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest'
      },
      responseType: 'json'
    })
    // ユーザーデータの取得
    console.log("userId:", this.userId)
    await axios.get(`/api/users/${this.userId}`).then(res => {
      console.log("user data")
      console.table(res.data)
      this.userData = res.data
    })
    // カテゴリーの取得
    await axios.get(`/api/categories/${this.userId}`).then(res => {
      console.log("categories data")
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
    flex-direction: column
    justify-content: center
    align-items: center
    padding-left: $side-bar-width
  &__input
    width: 200px
    margin-bottom: 1rem
  &__button
    margin-bottom: 1rem
    text-align: center
  &__table
    border-collapse: collapse
    line-height: 1.5rem
    width: 60%
    text-align: center
    border: 1px solid #B3B3B3
</style>