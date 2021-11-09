<template>
  <div>
    <div class="mypage__header">
      <Header />
    </div>
    <div>
      <!-- マイページのトップページ -->
      <side-bar
        :money="userData.money"
        :used_money="userData.used_money"
        :userId="userId"
      />
      <div class="mypage__main">
        <h4>{{ userData.name }}さんのマイページ</h4>
        <the-row>
          <div
            v-for="image in imageData" :key="image.id"
          >
            <div class="mypage__img">
              <img
                :src="`http://localhost:5000${image.image_url}`" alt="写真"
                class="mypage__img__body"
                @click="image.visible = true"
              />
              <el-dialog
                v-model="image.visible"
                :title="image.place"
                width="80%"
                center
              >
                <div class="mypage__modal">
                  <h3>{{ image.place }}</h3>
                  <div class="mypage__modal__img">
                    <img :src="`http://localhost:5000${image.image_url}`"  class="mypage__modal__img__body"/>
                  </div>
                  <h3>{{ image.act_time }}</h3>
                  <h3>{{ image.cost }}円</h3>
                  <div>
                    <el-rate v-model="image.score" disabled></el-rate>
                  </div>
                  <div>
                    <p>{{ image.diary }}</p>
                  </div>
                  <div>
                    <el-button @click="image.visible = false">Close</el-button>
                  </div>
                </div>
              </el-dialog>
            </div>
          </div>
        </the-row>
      </div>
    </div>
  </div>
</template>

<script>
import Header from '../../src/components/Header.vue'
import SideBar from '../../src/components/SideBar.vue'
import TheRow from '../../src/components/TheRow.vue'
// import MemoryModal from '../../src/components/MemoryModal.vue'
// import TheColumn from '../../src/components/TheColumn.vue'
// import TheSection from '../../src/components/TheSection.vue'
import Axios from 'axios'
import cookie from 'js-cookie'

export default {
  components: {
    Header,
    SideBar,
    TheRow,
    // MemoryModal,
    // TheColumn,
    // TheSection,
  },
  data () {
    return {
      imageData: [],
      userData: {},
      username: '',
      showConfirm: false
    }
  },
  props: {
    userId: {
      type: String,
      default: localStorage.getItem('userId')
    }
  },
  methods: {
    onModal() {
      this.visible = !this.visible
      console.log(this.visible)
    },
    confirm(event) {
      this.showConfirm = !this.showConfirm
      event.returnValue = "リロードするとログイン画面に戻ります"
    },
    saveUserId() {
      localStorage.setItem('userId', this.userId)
    }
  },
  // created() {
  //   window.addEventListener("beforeunload", this.confirm)
  // },
  mounted: async function () {
    // TODO:デプロイする際にurlを変更する
    const BASE_URL = "http://localhost:5000"
    cookie.set(this.userId)
    let axios = Axios.create({
      baseURL: BASE_URL,
      headers: {
        'Content-type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest'
      },
      responseType: 'json'
    })
    await axios.get(`/api/users/${this.userId}`).then(res => {
      console.log("user data")
      console.table(res.data)
      this.userData = res.data
    })
    await axios.get(`/api/images/${this.userId}`).then(res => {
      console.log("image data")
      console.table(res.data)
      const imageData = res.data
      imageData.map((image) => {
        this.imageData.push({
          id: image.id,
          act_time: image.act_time,
          cost: image.cost,
          diary: image.diary,
          file_name: image.file_name,
          image_url: image.image_url,
          score: image.score,
          user_id: image.user_id,
          visible: false
        })
      })
    })
    // this.$store.commit("setUserId", this.userId)
    this.saveUserId()
    cookie.set(this.userData)
    cookie.set(this.imageData)
  },
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
      height: 200px
      margin: 0 0.5rem 1rem
  &__modal
    &__img
      display: block
      text-align: center
      &__body
        max-width: 100%
</style>