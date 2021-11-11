<template>
  <div>
    <Header />
    <center>
    <i>
    <h1>
      nikki de kakeibo
    </h1>
    <div>
      <el-alert :title="alertMessage" :type="alertType"></el-alert>
    </div>
    <div>
      <h3 size="10">
        USER NAME
        <el-input
          placeholder="input user name"
          v-model="username"
          clearable
          class="login__input"
        />
      </h3>
    </div>
    <div>
      <h3>
        PASSWORD
        <el-input
          class="login__input"
          v-model="password"
          placeholder="input password"
          show-password
          width="180px"
        />
      </h3>
    </div>
    </i>
    <div>
      <div class="login__button">
        <el-button type="primary" plain @click="login">LOGIN</el-button>
      </div>
      <div class="login__button">
        <router-link to="/register">
          <el-button>
            NEW MEMBER
          </el-button>
        </router-link>
      </div>
    </div>
    </center>
  </div>
</template>

<script>
import cookie from 'js-cookie'
import Axios from 'axios'
import crypto from 'crypto'
import router from '../src/router'
import Header from '../src/components/Header.vue'

export default {
  data () {
    return {
      userId: '',
      username: '',
      password: '',
      alertMessage: '',
      alertType: '',
    }
  },
  components: {
    Header,
  },
  methods: {
    login () {
      // BASE_URL→公開時とlocalhost時で適宜変更する必要がある
      const BASE_URL = 'https://nikkidekakeibo.azurewebsites.net/'
      // const BASE_URL = "http://localhost:5000"
      let sha256 = crypto.createHash('sha256')
      sha256.update(this.password)
      const hashPass = sha256.digest('base64')

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
        '/api/login',
        {
          username: self.username,
          password: hashPass
        },
        {
          validationStatus: function (status) {
            return status < 500
          }
        }
      )
      .then(res  => {
        if (res.data.access_token) {
          console.table(res.data)
          cookie.set('jwt_token', res.data.access_token)
          // TODO:ルーターを介してユーザー情報をpropsで渡す
          router.push({
            name: 'MyPage',
            params: {
              username: self.username,
              userId: res.data.user_id
            }
          })
        } else if (res.status === 401) {
          // ユーザー名とパスワードが間違っていた場合
          self.alertType = 'error'
          self.alertMessage = 'ユーザー名またはパスワードが違います'
        } else {
          throw new Error()
        }
      })
      .catch(() => {
        // エラー発生時(例外処理)
        console.log('failed')
        self.alertType = 'error'
        self.alertMessage = 'エラーが発生しました'
      })
    }
  }
}
</script>

<style lang="sass" scoped>
.login
  &__input
    width: 180px
  &__button
    margin-bottom: 1rem
</style>
