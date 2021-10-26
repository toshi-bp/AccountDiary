<template>
  <div>
    <div class="mypage__header">
      <Header />
    </div>
    <div>
      <!-- マイページのトップページ -->
      <side-bar />
      <div class="mypage__main">
        <the-row>
          <div
            v-for="i in 21" :key="i"
          >
            <div class="mypage__img">
              <img
                src="https://1.bp.blogspot.com/-tVeC6En4e_E/X96mhDTzJNI/AAAAAAABdBo/jlD_jvZvMuk3qUcNjA_XORrA4w3lhPkdQCNcBGAsYHQ/s1048/onepiece01_luffy.png" alt="カレー"
                class="mypage__img__body"
                @click="onModal"
              />
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
// import TheColumn from '../../src/components/TheColumn.vue'
// import TheSection from '../../src/components/TheSection.vue'

export default {
  components: {
    Header,
    SideBar,
    TheRow,
    // TheColumn,
    // TheSection,
  },
  data () {
    return {
      visible: false
    }
  },
  methods: {
    onModal() {
      this.visible = !this.visible
      console.log(this.visible)
    }
  }
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