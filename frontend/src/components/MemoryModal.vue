<template>
  <div>
    <!-- 写真をクリックしたらその詳細がモーダルとして出てくるやつ -->
    <el-dialog
      :title="name"
      :v-model:visible="$props.isVisible"
      width="80%"
    >
      <div>
        <img :src="imageUrl"/>
      </div>
      <h3>{{ title }}：{{ cost }}円</h3>
      <div>
        <el-rate v-model="score"></el-rate>
      </div>
      <div v-for="hashTag in hashTags" :key="hashTag">
        <h4>{{ hashTag }}</h4>
      </div>
      <div>
        <p>{{ description }}</p>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  props: {
    isVisible: {
      type: Boolean
    },
    date: {
      type: Date,
    },
    name: {
      type: String,
    },
    imageUrl: {
      type: String
    },
    title: {
      type: String
    },
    cost: {
      type: Number
    },
    hashTags: {
      type: Array
    },
    description: {
      type: String,
    },
  },
  computed: {
    getMonth: function(date) {
      return date.getMonth()
    },
    
  }
}
</script>

<style lang="sass" scoped>

</style>