<template>
  <div>
    <Header />
    <center>
    <i>
    <h1>
      nikki de kakeibo
    </h1>
    <div>
      <p v-if="snackbar">
        {{ snackbarText }}
      </p>
    </div>
    <div>
      <h3 size="10">
        <!-- ユーザー名の方がわかりやすいのではないか？と思った -->
        USER ID
        <el-input
          placeholder="input id"
          v-model="userId"
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
          type="text"
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
        <el-button type="primary" plain>LOGIN</el-button>
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
      password: '',
      snackbarText: '',
    }
  },
  components: {
    Header,
  },
  methods: {
    signin () {
      // BASE_URL→公開時とlocalhost時で適宜変更する必要がある
      const BASE_URL = "http://loalhost/3000"
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
        'signin',
        {
          userId: self.userId,
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
          cookie.set('jwt_token', res.data.access_token)
          // TODO:ルーターの設定を見直す
          router.push({ name: 'user' })
        } else if (res.status === 401) {
          // ユーザー名とパスワードが間違っていた場合
          self.snackbarText = 'ユーザー名またはパスワードが違います'
        } else {
          throw new Error()
        }
      })
      .catch(() => {
        // エラー発生時(例外処理)
        self.snackbarText = 'エラーが発生しました'
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
