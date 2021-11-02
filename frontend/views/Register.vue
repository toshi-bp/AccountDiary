<template>
  <div>
    <Header />
    <router-link to="/login">
    <div style="text-align: right;">BACK
    </div>
    </router-link>
    <center>
      <h3>新規登録</h3>
      <el-alert :title="alertMessage" :type="alertType">
      </el-alert>
    <i>
      <div>
        MAIL Address
        <el-input v-model="mail" class="register__input" />
      </div>
      <div>
        NAME
        <el-input v-model="name" class="register__input" />
      </div>
      <div>
        PASSWORD
        <el-input v-model="password" class="register__input" />
      </div>
      <div>
        CONFIRM PASSWORD
        <el-input v-model="passwordConf" class="register__input" />
      </div>
      <div  style="margin-bottom: 1rem;">
        BIRTH DAY
        <el-date-picker v-model="birthday" placeholder="enter your birthday" class="register__input"/>
      </div>
      <div>
        GENDER
        <el-select v-model="gender" class="register__input">
          <el-option
            v-for="item in genders"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          />
        </el-select>
      </div>
      <div>
        TELL NUMBER
        <el-input v-model="phone1" class="register__input">
          <template>-</template>
        </el-input>
      </div>
      <div>
        <div><el-button type="primary" plain @click="register">SEND</el-button></div>
      </div>
      </i>
      </center>
  </div>
</template>

<script>
import Axios from 'axios'
import crypto from 'crypto'
import router from '../src/router'
import Header from '../src/components/Header.vue'

export default {
  data () {
    return {
      mail: '',
      password: '',
      passwordConf: '',
      birthday: '',
      genders: [
        {
          value: 'male',
          label: '男'
        },
        {
          value: 'female',
          label: '女'
        },
        {
          value: 'other',
          label: 'その他'
        }
      ],
      name: '',
      gender: '',
      phone: '',
      phone1: '000',
      phone2: '111',
      phone3: '2222',
      alertMessage: '',
      alertType: '',
    }
  },
  components: {
    Header,
  },
  computed: {
    generateUserId() {
      const strong = 1000
      return new Date().getTime().toString(16)  + Math.floor(strong*Math.random()).toString(16)
    },
  },
  methods: {
    register () {
      const BASE_URL = 'http://localhost:5000'
      if (this.mail === '' || this.birthday === '') {
        return
      }
      if (this.password !== this.passwordConf) {
        return
      }
      // 誕生日は文字列+/として格納
      const year = this.birthday.getFullYear()
      const month = this.birthday.getMonth() + 1
      const date = this.birthday.getDate()
      const birthday = year.toString() + '/' + month.toString() + '/' + date.toString()
      let sha256 = crypto.createHash('sha256')
      sha256.update(this.password)
      const hashPass = sha256.digest('base64')

      let sha256Conf = crypto.createHash('sha256')
      sha256Conf.update(this.passwordConf)
      const hashPassConf = sha256.digest('base64')
      console.log(hashPassConf)
      const user_id = this.generateUserId
      console.log(user_id)

      const phoneNumber = this.phone1 + this.phone2 + this.phone3
      let axios = Axios.create({
        baseURL: BASE_URL,
        headers: {
          'Content-Type': 'application/json',
          'X-Requested-With': 'XMLHttpRequest'
        },
        responseType: 'json'
      })
      let self = this
      axios.post('/api/users/add', {
        id: user_id,
        mail: self.mail,
        password: hashPass,
        name: self.name,
        birthday: birthday,
        gender: self.gender,
        phone: phoneNumber,
      })
      .then(res => {
        console.log(res)
        this.alertMessage = '登録成功'
        this.alertType = 'success'
        // 登録成功した際の処理
        setTimeout(function () {
          router.push({ name: 'Login' })
        }, 1500)
      })
      .catch(() => {
        console.log('error')
        this.alertMessage = 'エラー'
        this.alertType = 'error'
      })
    }
  }
}
</script>

<style lang="sass" scoped>
.register
  &__input
    width: 180px
    margin-bottom: 1rem
</style>