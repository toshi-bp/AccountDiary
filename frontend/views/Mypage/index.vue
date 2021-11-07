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
                @click="onModal"
              />
              <div>
                <!-- <memory-modal
                  :cost="1000"
                  :description="'今日はタカシとカレー。美味しかった。'"
                  :date="new Date('July 20, 69 00:20:18')"
                  :imageUrl="'https://1.bp.blogspot.com/-tVeC6En4e_E/X96mhDTzJNI/AAAAAAABdBo/jlD_jvZvMuk3qUcNjA_XORrA4w3lhPkdQCNcBGAsYHQ/s1048/onepiece01_luffy.png'"
                  :hashTags="['タカシ', '洋風カレー']"
                  :isVisible="visible"
                  :name="'洋風カレー'"
                  :title="'ABCカレー'"
                /> -->
              </div>
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
      visible: false,
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
      this.imageData = res.data
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
      margin: 0 0.5rem 1rem
</style>