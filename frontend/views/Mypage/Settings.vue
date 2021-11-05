<template>

<div>
 <SideBar/>
 <center>
 
 <h1>カテゴリー名の変更</h1>
 <p><h10>------変更前------</h10></p>
 <el-select v-model="value" placeholder="Select">
    <el-option
      v-for="item in options"
      :key="item.value"
      :label="item.label"
      :value="item.value">
    </el-option>
 </el-select>
 <p><h10>------変更後------</h10></p>
 <input v-model="message1" placeholder="edit me" size="30">
 <p></p>
 <button type="submit">送信する</button>
 <hr size="5" noshade="" color="#000">
 <h1>予算の設定</h1>
 <input v-model="message2" placeholder="edit me" size="30">
 <p></p>
 <button type="submit">送信する</button>
 <hr size="5" noshade="" color="#000" >
 <h1>個人情報</h1>
 <p><h10>------アカウント確認------</h10></p>
 <input v-model="message3" placeholder="edit me" size="30">
 <p></p>
 <button type="submit">送信する</button>
 <p><h10>------パスワード変更------</h10></p>
 <input v-model="message4" placeholder="edit me" size="30">
 <p></p>
 <button type="submit">送信する</button>
 <hr size="5" noshade="" color="#000">
 </center>
</div>
</template>


<script>
  import SideBar from '../../src/components/SideBar.vue'
  export default {
    components:{
      SideBar,
    },
    data() {
      return {
        options: [{
          value: 'Option1',
          label: 'Option1'
        }, {
          value: 'Option2',
          label: 'Option2'
        }, {
          value: 'Option3',
          label: 'Option3'
        }, {
          value: 'Option4',
          label: 'Option4'
        }, ],
        value: ''
      }
    },

    data1() {
     return {
      input: ''
     }
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