<template>
  <div>
    <!-- 写真をクリックしたらその詳細がモーダルとして出てくるやつ -->
    <el-dialog
      v-model="memoryVisible"
      :title="place"
      width="80%"
      :before-close="handleClose"
    >
      <div>
        <!-- <img :src="`https://nikkidekakeibo.azurewebsites.net/${imageUrl}`"/> -->
        <img :src="`http://localhost:5000${imageUrl}`"/>
      </div>
      <h3>{{ date }}</h3>
      <h3>{{ cost }}円</h3>
      <div>
        <el-rate v-model="memoryScore" disabled></el-rate>
      </div>
      <div>
        <p>{{ description }}</p>
      </div>
      <div>
        <el-button @click="closeModal">Close</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data () {
    return {
      memoryScore: this.score,
      memoryVisible: this.isVisible
    }
  },
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
    score: {
      type: Number
    }
  },
  methods: {
    closeModal() {
      this.$emit('close')
    }
  }
}
</script>

<style lang="sass" scoped>

</style>