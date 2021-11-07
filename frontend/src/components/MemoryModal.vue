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
      <h3>{{ date }}</h3>
      <h3>{{ title }}：{{ cost }}円</h3>
      <h4>場所: {{ place }}</h4>
      <div>
        <el-rate v-model="score"></el-rate>
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
      type: String,
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
    description: {
      type: String,
    },
    place: {
      type: String,
    },
  },
  computed: {
  }
}
</script>

<style lang="sass" scoped>

</style>