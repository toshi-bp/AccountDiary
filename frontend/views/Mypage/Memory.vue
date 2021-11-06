<template>
  <div>
    <center>
      <div>
        <el-alert :title="alertMessage" :type="alertType"></el-alert>
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
      <el-option-group
          v-for="group in options"
          :key="group.label"
          :label="group.label">
        <el-option
          v-for="item in group.options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-option-group>
      </el-select>
    </div>
    <!-- 場所入力 -->
    場所を入力してね
    <div>
      <el-input v-model="place" placeholder="Please input" />
    </div>
    <!-- ひとこと入力 -->
    ひとことを入力してね
    <div>
      <el-input v-model="diary" placeholder="Please input" />
    </div>
    <div>
      <el-upload
        class="upload-demo"
        action="https://jsonplaceholder.typicode.com/posts/"
        :on-preview="handlePreview"
        :on-remove="handleRemove"
        :before-remove="beforeRemove"
        multiple
        :limit="3"
        :on-exceed="handleExceed"
        :file-list="fileList"
      >
        <el-button size="small" type="primary">Click to upload</el-button>
        <template #tip>
          <div class="el-upload__tip">
            jpg/png files with a size less than 500kb
          </div>
        </template>
      </el-upload>
    </div>
    <div>
      <el-row>
        <el-button type="primary" plain @click="upload">保存</el-button>
      </el-row>
    </div>
    </center>
  </div>
</template>

<script>
// import { reactive, toRefs } from 'vue'
import Axios from 'axios'

export default {
  // setup() {
  //   const state = reactive({
  //     disabledDate(time) {
  //       return time.getTime() > Date.now()
  //     },
  //     shortcuts: [
  //       {
  //         text: 'Today',
  //         value: new Date(),
  //       },
  //       {
  //         text: 'Yesterday',
  //         value: () => {
  //           const date = new Date()
  //           date.setTime(date.getTime() - 3600 * 1000 * 24)
  //           return date
  //         },
  //       },
  //       {
  //         text: 'A week ago',
  //         value: () => {
  //           const date = new Date()
  //           date.setTime(date.getTime() - 3600 * 1000 * 24 * 7)
  //           return date
  //         },
  //       },
  //     ],
  //     value1: '',
  //     value2: '',
  //   })
  //   return {
  //     ...toRefs(state),
  //   }
  // },
  // 支出or収入
  data() {
    return {
      types: [{
        id: 1,
        value: 'income',
        label: '支出'
      }, {
        id: 2,
        value: 'expenditure',
        label: '収入'
      }
      ],
      value: '',
      // ↓収入or支出
      type: '',
      date: '',
      cost: 0,
      alertMessage: '',
      alertType: '',
      place: '',
      diary: '',
      category: '',
      fileList: [
        {
          name: 'food.jpeg',
          url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100',
        },
        {
          name: 'food2.jpeg',
          url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100',
        },
      ],
    }
  },
  props: {
    userId: {
      type: String
    }
  },
  methods: {
    // handleRemove(file, fileList) {
    //   console.log(file, fileList)
    // },
    // handlePreview(file) {
    //   console.log(file)
    // },
    // handleExceed(files, fileList) {
    //   this.$message.warning(
    //     `The limit is 3, you selected ${
    //       files.length
    //     } files this time, add up to ${files.length + fileList.length} totally`
    //   )
    // },
    // beforeRemove(file) {
    //   return this.$confirm(`Cancel the transfert of ${file.name} ?`)
    // },
    upload () {
      // TODO:公開する際にurlを変更
      const BASE_URL = "http://localhost:5000"
      const axios = Axios.create({
        baseURL: BASE_URL,
        headers: {
          'Content-type': 'application/json',
          'X-Requested-With': 'XMLHttpRequest'
        },
        responseType: 'json'
      })
      let self = this
      axios.post(
        '/api/histories/add',
        {
          // 登録するデータ
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
    }
  }
}
</script>

<style lang="sass" scoped>
.memory
  // 何か書く
    &__input
      // 何か書く
</style>

