<template>
  <div class="menu">
    <div class="side-bar-sp">
      <button
        class="side-bar-sp__toggle"
        :class="{ '--active': active }"
        @click="toggle"
      >
        <fa :icon="active ? 'times' : 'bars'" fixed-width/>
      </button>
      <div class="side-bar-sp__toggle__square" />
      <div
        class="side-bar-sp__bg"
        :class="{ '--active':active }"
      />
      <nav class="side-bar-sp__body" :class="{ '--active' : active }">
        <h3>Menu</h3>
        <ul
          v-for="item in menu" :key="item.id"
          class="side-bar-sp__list__body"
        >
          <router-link :to="{path: item.path, name: item.name, params: { userId: userId }}">
            <li class="side-bar-sp__list__body__item">
              {{ item.title }}
            </li>
          </router-link>
        </ul>
      </nav>
    </div>
    <div class="side-bar">
      <div class="side-bar__list">
        <h3>Menu</h3>
        <ul
          v-for="item in menu" :key="item.id"
          class="side-bar__list__body"
        >
          <router-link :to="{path: item.path, name: item.name, params: { userId: userId }}">
            <li class="side-bar__list__body__item">
              {{ item.title }}
              <!-- name:{{ item.name }}<br />
              userid:{{ userId }} -->
            </li>
          </router-link>
        </ul>
      </div>
      <div>
        <div class="side-bar__money">
          <!-- データベースから取ってきたデータを元に表示する形式に変更 -->
          <h3>予算</h3>
          <p>{{ money }}円</p>
          <h3>使用金額</h3>
          <p>{{ used_money }}円</p>
          <hr />
          <h3>
            使用可能金額
          </h3>
          <p>
            {{ canUseMoney }}円
          </p>
          <div v-if="used_money / money > 0.8">
            <el-alert></el-alert>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      // pathを後で書き直す
      menu: [
        {
          id: 1,
          title: "トップ",
          path: "/mypage/",
          name: "MyPage"
        },
        {
          id: 2,
          title: "入力",
          path: "/mypage/memory",
          name: "Memory"
        },
        {
          id: 3,
          title: "履歴",
          path: "/mypage/table",
          name: "Table"
        },
        {
          id: 4,
          title: "分析",
          path: "/mypage/analytics",
          name: "Analytics"
        },
        {
          id: 5,
          title: "設定",
          path: "/mypage/settings",
          name: "Settings"
        }
      ]
    }
  },
  props: {
    userId: {
      type: String
    },
    money: {
      type: Number,
      default: 0
    },
    used_money: {
      type: Number,
      default: 0
    }
  },
  computed: {
    canUseMoney() {
      const diff = this.money - this.used_money
      if (diff > 0) {
        return diff
      } else {
        return 0
      }
    }
  },
  methods: {
    saveUserId() {
      localStorage.setItem('userId', this.userId)
    },
  },
  mounted() {
    this.saveUserId()
  }
}
</script>

<style lang="sass" scoped>
@import '~bootstrap/scss/mixins/_breakpoints'
$grid-breakpoints: (xs: 0, sm: 576px, md: 768.2px, mmd:860px, lg: 992px, xl: 1200px, wd: 1500px)
.side-bar
  display: block
  position: fixed
  top: 0
  left: 0
  width: 256px
  min-height: 100vh
  background-color: #282a34
  // background-color: #9ce0e0
  &__list
    display: flex
    flex-direction: column
    align-items: center
    color: #fff
    &__body
      list-style: none
      margin-left: -2.7rem
      &__item
        color: #fff
        text-decoration: none
  &__money
    color: #fff
    text-align: center
  @include media-breakpoint-down(sm)
    display: none

.side-bar-sp
  &__toggle
    appearance: none
    position: fixed
    bottom: 2rem
    right: 2rem
    z-index: 9400
    background: #ffffff
    border: 2px solid #000
    line-height: 1
    color: #000
    width: 3.5rem
    height: 3.5rem
    box-shadow: 0.1rem 0.1rem 0 rgba(#000, 0.2)
    outline: none
    transition: 0.2s ease background, 0.2s ease color
    &--active
      background: #ffffff
      color: #282a34
    &:hover
      background: #282a34
      color: #ffffff
    &:focus
      box-shadow: 0.1rem 0.1rem 0 rgba(#000, 0.2)

    &__square
      appearance: none
      position: fixed
      bottom: 4.2rem
      right: 4.3rem
      background: #ffffff
      border: solid #000
      border-width: 2px
      width: 2rem
      height: 2rem
      box-shadow: 0.1rem 0.1rem 0 rgba(#000, 0.1)
      z-index: 9500
  
  &__body
    position: fixed
    top: 0
    bottom: 0
    left: 0
    width: 100%
    max-width: 256px
    z-index: 9550
    background: #fff
    padding-bottom: 7rem

  &__bg
    position: fixed
    top: 0
    bottom: 0
    left: 0
    right: 0
    background: rgba(#282a34, 0.75)
    z-index: 9200
  &__list
    display: flex
    flex-direction: column
    align-items: center
    color: #fff
    &__body
      list-style: none
      margin-left: -2.7rem
      &__item
        color: #fff
        text-decoration: none
  &__money
    color: #fff
    text-align: center
  @include media-breakpoint-up(sm)
    display: none
</style>