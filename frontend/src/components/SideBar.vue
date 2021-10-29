<template>
  <div class="side-bar">
    <div class="side-bar__list">
      <h3>Menu</h3>
      <ul
        v-for="item in menu" :key="item.id"
        class="side-bar__list__body"
      >
        <router-link :to="item.path">
          <li class="side-bar__list__body__item">{{ item.title }}</li>
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
        <p v-if="canUseMoney <= 0">
          赤字
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      money: 60000,
      used_money: 40000,
      // pathを後で書き直す
      menu: [
        {
          id: 1,
          title: "トップ",
          path: "/mypage"
        },
        {
          id: 2,
          title: "入力",
          path: "/mypage/memory"
        },
        {
          id: 3,
          title: "履歴",
          path: "/mypage/memory"
        },
        {
          id: 4,
          title: "分析",
          path: "/mypage/memory"
        },
        {
          id: 5,
          title: "設定",
          path: "/mypage/memory"
        }
      ]
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
  }
}
</script>

<style lang="sass" scoped>
.side-bar
  display: block
  position: fixed
  top: 0
  left: 0
  width: 256px
  height: 100vh
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
</style>