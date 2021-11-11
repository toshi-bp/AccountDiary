<template>
  <!--
      LPpageをここで記述していきます。
      コード自体は初めて書くので、とても汚いかもしれませんが
      どうかお許しください。
    -->

  <el-container>
    <el-header>
      <font size="8" color="#606266" face="San Francisco UI">
        <i> nikki de kakeibo </i>
      </font>
    </el-header>

    <el-main>
      <p>
        <el-carousel :interval="5000" arrow="always">
          <el-carousel-item v-for="item in 4" :key="item">
            <h3>{{ item }}</h3>
          </el-carousel-item>
        </el-carousel>
      </p>
      <p>
        <el-row>
          <el-col :span="12"><div class="grid-content bg-purple">
            あなたのSEKAIを変える
          </div></el-col>
          <el-col :span="12"><div class="grid-content bg-purple-light">
            BE THE CHANGE
          </div></el-col>
        </el-row>
      </p>
      <p>使い方はこうです。</p>
      <p>さぁ、始めましょう。</p>
    </el-main>

    <el-footer>
      <el-footcopy> Copyright © 2021 MASSH Group C </el-footcopy>
    </el-footer>
  </el-container>
</template>

<script>
export default {};
</script>

<style scoped>
.el-header,
.el-footer {
  background-color: #f8e788;
  color: #333;
  text-align: center;
  line-height: 60px;
}

.el-main {
  background-color: #fdf39a;
  color: #333;
  text-align: center;
  line-height: 160px;
}
.el-carousel__item h3 {
  color: #475669;
  font-size: 18px;
  opacity: 0.75;
  line-height: 300px;
  margin: 0;
}
.bg-purple {
  background: #9ef093;
}

.bg-purple-light {
  background: #a7f7e9;
}
</style>