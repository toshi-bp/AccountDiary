<template>
  <div>
    <div>
      <side-bar
        :userId="this.userId"
        :money="userData.money"
        :used_money="userData.used_money"
      />
    </div>
    <div class="memory__main">
      <div>
        <el-alert :title="alertMessage" :type="alertType" v-if="alertType !== ''"></el-alert>
      </div>
      <h3>記録</h3>
      <!-- 支出収入選択 -->
      支出収入を選択してね
      <div>
        <el-select v-model="type" placeholder="Select">
          <el-option
            v-for="item in types"
            :key="item.id"
            :label="item.label"
            :value="item.value"
          >
          </el-option>
        </el-select>
      </div>
      <!-- 日付入力 -->
      日付を選択してね
      <div class="demo-date-picker">
        <div class="block">
          <span class="demonstration"></span>
          <el-date-picker
            v-model="date"
            type="date"
            placeholder="Pick a day"
            :disabled-date="disabledDate"
            :shortcuts="shortcuts"
          >
          </el-date-picker>
        </div>
      </div>
      <!-- 金額入力 -->
      金額を入力してね
      <div>
        <el-input-number v-model="cost" :step="100" />
      </div>
      <!-- カテゴリ選択 -->
      カテゴリを選択してね
      <div>
        <el-select v-model="category" placeholder="Select">
          <el-option
            v-for="item in categoryFilter"
            :key="item.type"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>
      </div>
      <!-- 場所入力 -->
      場所を入力してね
      <div class="memory__input">
        <el-input v-model="place" placeholder="Please input" />
      </div>
      <!-- ひとこと入力 -->
      ひとことを入力してね
      <div class="memory__input">
        <el-input v-model="diary" placeholder="Please input" autosize type="textarea"/>
      </div>
      <div class="memory__image">
        <input type="file" accept="image/*" @change="onUploadImage"/>
        <!-- <el-button size="small" type="primary">Click to upload</el-button> -->
      </div>
      <div>
        <!--思い出のスコアを選択-->
        <p>思い出のスコアを選択してください</p>
        <el-rate v-model="score"></el-rate>
        score:{{ score }}
      </div>
      <div class="memory__button">
        <el-button type="primary" plain @click="upload">保存</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import SideBar from '../../src/components/SideBar.vue'
import Axios from 'axios'

export default {
  // 支出or収入
  data() {
    return {
      types: [{
        id: 1,
        value: 'income',
        label: '収入'
      }, {
        id: 2,
        value: 'expenditure',
        label: '支出'
      }],
      value: '',
      // ↓収入or支出(income or expenditure)
      type: 'income',
      date: '',
      cost: 0,
      alertMessage: '',
      alertType: '',
      place: '',
      diary: '',
      category: '',
      categories: [
        {
          type: 'income',
          label: '給与',
          value: '給与',
        },
        {
          type: 'income',
          label: 'その他の収入',
          value: 'その他の収入',
        },
        {
          type: 'expenditure',
          label: '生活費',
          value: '生活費',
        },
        {
          type: 'expenditure',
          label: '趣味・娯楽',
          value: '趣味・娯楽',
        },
      ],
      userData: {},
      score: 0,
      file_name: '',
      image_url: '',
    }
  },
  props: {
    userId: {
      type: String,
      default: localStorage.getItem('userId')
    }
  },
  components: {
    SideBar,
  },
  computed: {
    categoryFilter() {
      return this.categories.filter(item => item.type === this.type)
    }
  },
  methods: {
    async onUploadImage(e) {
      const file = e.target.files[0]
      this.file_name = file.name
      let reader = new FileReader
      reader.onload = (e) => {
        this.image_url = e.target.result
      }
      reader.readAsDataURL(file)
      let params = new FormData
      params.append('image', this.image_url)
      console.table(params)
      this.image_url = params
    },
    saveUserId() {
      localStorage.setItem('userId', this.userId)
    },
    handlePreview(file) {
      console.log(file)
    },
    async upload () {
      console.log(this.filename)
      console.log("type:" + this.type)
      // 日付を文字列に変換
      const year = this.date.getFullYear()
      const month = this.date.getMonth() + 1
      const date = this.date.getDate()
      const act_time = year.toString() + '/' + month.toString() + '/' + date.toString()
      console.log(act_time)
      // TODO:公開する際にurlを変更
      // const BASE_URL = "http://localhost:5000"
      const BASE_URL = 'https://nikkidekakeibo.herokuapp.com'
      const axios = Axios.create({
        baseURL: BASE_URL,
        headers: {
          'Content-type': 'application/json',
          'X-Requested-With': 'XMLHttpRequest'
        },
        responseType: 'json'
      })
      let self = this

      // historiesにデータを追加
      await axios.post(
        '/api/histories/add',
        {
          // 登録するデータ
          user_id: self.userId,
          action: self.diary,
          result: self.cost,
          act_time: act_time,
          update_time: act_time,
          type: self.type,
          category: self.category,
          place: self.place
        }
      )
      .then (res => {
        console.table(res.data)
      })
      .catch(() => {
        // エラー発生時(例外処理)
        console.log('failed')
        self.alertType = 'error'
        self.alertMessage = 'エラーが発生しました'
      })
      // imagesにデータを追加
      if (this.filename !== '') {
        await axios.post(
          '/api/images/add',
          {
            user_id: self.userId,
            image_url: self.image_url,
            file_name: self.file_name,
            act_time: act_time,
            update_time: act_time,
            diary: self.diary,
            score: self.score,
            cost: self.cost,
          }
        ).then (res => {
          console.table(res.data)
        })
        .catch(() => {
          // エラー発生時(例外処理)
          console.log('failed')
          self.alertType = 'error'
          self.alertMessage = 'エラーが発生しました'
        })
      }
      // usersのmoneyをアップデート
      await axios.patch(
        `/api/users/update_money/${self.userId}`,
        {
          user_id: self.userId,
          money: self.cost,
          type: self.type
        }
      ).then(res => {
        console.log(res.data)
      })
    }
  },
  mounted: async function() {
    // TODO:ページを開いた際にそれぞれのユーザーのカテゴリーを取得する
    console.log(this.userId)
    const BASE_URL = "http://localhost:5000"
    let axios = Axios.create({
      baseURL: BASE_URL,
      headers: {
        'Content-type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest'
      },
      responseType: 'json'
    })
    await axios.get(`/api/users/${this.userId}`).then(res => {
      this.userData = res.data
    })
    await axios.get(`/api/categories/${this.userId}`).then(res => {
      // apiから取得したデータを表示用の構造に書き換える
      res.data.map(item => {
        this.categories.push({
          type: item.type,
          label: item.category,
          value: item.category
        })
      })
    })
    await this.saveUserId()
  },
}
</script>

<style lang="sass" scoped>
.memory
  $side-bar-width: 256px
  $main-width: calc(100% - #{$side-bar-width})
  &__main
    padding-left: $side-bar-width
    text-align: center
  &__input
    width: 250px
    margin: 0 auto 1rem
  &__button
    margin-top: 1.5rem
</style>
