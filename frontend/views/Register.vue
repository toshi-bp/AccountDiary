<template>
  <div>
    <Header />
    <pre>
    <div style="text-align: right;">BACK
    </div>
    <center>
    <i>
      MAIL Address <input type="text" size="15" maxlength="20" v-model="mail">
      PASSWORD  <input type="password" size="15" maxlength="20" v-model="password">
      <div>
        BIRTH DAY
        <el-date-picker size="15" maxlength="20" v-model="birthday" placeholder="enter your birthday"/>
      </div>
      GENDER
      <el-select size="15" maxlength="20" v-model="gender">
        <el-option
          v-for="item in genders"
          :key="item.value"
          :label="item.label"
          :value="item.value"
        />
      </el-select>
      TELL NUMBER<input type="text" size="15" maxlength="20" v-model="phone">
      <div>
        <div><a href='Signin.vue'><el-button type="primary" plain>SEND</el-button></a></div>
      </div>
      </i>
      </center>
      </pre>
  </div>
</template>

<script>
// import Axios from 'axios'
// import crypto from 'crypto'
import Header from '../src/components/Header.vue'

export default {
  data () {
    return {
      mail: '',
      password: '',
      birthday: Date,
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
      gender: '',
      phone: ''
    }
  },
  components: {
    Header,
  }
}
</script>