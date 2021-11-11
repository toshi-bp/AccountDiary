<template>
  <!--
      LPpageをここで記述していきます。
      コード自体は初めて書くので、とても汚いかもしれませんが
      どうかお許しください。
    -->

  <el-container>
    <el-header>
      <font size="8" color="#fff" face="San Francisco UI">
        <i> nikki de kakeibo </i>
      </font>
    </el-header>

    <el-main>
      <p>
        <el-carousel :interval="5000" arrow="always">
          <el-carousel-item>
            <img
              src="@/assets/img/ex_graph.png"
              alt="Logo"
              class="main__logo1"
            />
          </el-carousel-item>
          <el-carousel-item>
            <img
              src="@/assets/img/ex_image.png"
              alt="Logo"
              class="main__logo1"
            />
          </el-carousel-item>
          <el-carousel-item>
            <img
              src="@/assets/img/ex_Mypage.png"
              alt="Logo"
              class="main__logo1"
            />
          </el-carousel-item>
          <el-carousel-item>
            <img
              src="@/assets/img/ex_table.png"
              alt="Logo"
              class="main__logo1"
            />
          </el-carousel-item>
        </el-carousel>
      </p>
      <p>
        <el-row>
          <el-col :span="12"
            ><div class="grid-content bg-purple">
              あなたのSEKAIを変える
            </div></el-col
          >
          <el-col :span="12"
            ><div class="grid-content bg-purple-light">
              BE THE CHANGE
            </div></el-col
          >
        </el-row>
      </p>
      <section>
        <h2 class="ttl">使い方</h2>
        <el-row>
          <el-col :span="12"
            ><div>
              <img
                src="@/assets/img/login.jpg"
                alt="Logo"
                class="main__logo1"
              /></div
          ></el-col>
          <el-col :span="12"
            ><div>
              <li>まずは、ログインをしよう！</li>
            </div></el-col
          >
        </el-row>
        <el-row>
          <el-col :span="12"
            ><div><li>登録が済んでない人は登録から！</li></div></el-col
          >
          <el-col :span="12"
            ><div>
              <img
                src="@/assets/img/register.jpg"
                alt="Logo"
                class="main__logo1"
              /></div
          ></el-col>
        </el-row>
        <el-row>
          <el-col :span="12"
            ><div>
              <img
                src="@/assets/img/login.jpg"
                alt="Logo"
                class="main__logo1"
              /></div
          ></el-col>
          <el-col :span="12"
            ><div>
              <li>まずは、ログインをしよう！</li>
            </div></el-col
          >
        </el-row>
      </section>

      <p>さぁ、始めましょう。</p>
    </el-main>

    <el-footer>
      <font size="3" color="#000000" face="San Francisco UI">
        <i> Copyright © 2021 MASSH Group C</i>
      </font>
    </el-footer>
  </el-container>
</template>

<script>
export default {};
</script>

<style scoped>
.el-header {
  background-color:#282a34;
  color: #333;
  text-align: center;
  line-height: 60px;
}
.el-footer {
  background:linear-gradient(#e0a21a, #463c04);
  color: #333;
  text-align: center;
  line-height: 60px;
}

.el-main {
  background-color: #f8f8de;
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
.main__logo1 {
  width: 100%;
  height: 100%;
}
</style>