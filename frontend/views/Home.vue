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
      <el-row :gutter="20">
        <el-col :span="12" :offset="6"
          ><div class="grid-content bg-purple">
            <el-carousel :interval="5000" arrow="always">
              <el-carousel-item>
                <img
                  src="@/assets/img/image1.jpg"
                  alt="Logo"
                  class="main__logo1"
                />
              </el-carousel-item>
              <el-carousel-item>
                <img
                  src="@/assets/img/image2.jpg"
                  alt="Logo"
                  class="main__logo1"
                />
              </el-carousel-item>
              <el-carousel-item>
                <img
                  src="@/assets/img/image3.jpg"
                  alt="Logo"
                  class="main__logo1"
                />
              </el-carousel-item>
              <el-carousel-item>
                <img
                  src="@/assets/img/image4.jpg"
                  alt="Logo"
                  class="main__logo1"
                />
              </el-carousel-item>
            </el-carousel></div
        ></el-col>
      </el-row>

    </el-main>
                <img
                  src="@/assets/img/onayami.png"
                  alt="Logo"
                  class="main__logo1"
                />
      <el-main>
      <p>
        <el-row>
          <el-col :xs="8" :sm="6" :md="4" :lg="3" :xl="1"><div></div></el-col>
          <el-col :xs="4" :sm="6" :md="8" :lg="9" :xl="11"
            ><div>
              <img
                src="@/assets/img/nayami.jpg"
                alt="Logo"
                class="main__logo1"
              /></div
          ></el-col>
          <el-col :xs="4" :sm="6" :md="8" :lg="9" :xl="11"
            ><div>
              <h1>最近、気が付いたらお金が減っている。</h1>
              <h3>本当は貯金したいのに。。。</h3>
            </div></el-col
          >
          <el-col :xs="8" :sm="6" :md="4" :lg="3" :xl="1"><div></div></el-col>
        </el-row>
      </p>
      <p>
        <font size="5" color="#000000" face="San Francisco UI">
          <i> 皆さん、家計簿めんどくさいですよね。</i>
        </font>
      </p>
            <p>
        <font size="5" color="#000000" face="San Francisco UI">
          <i> 家計簿の現状。ご存知ですか？</i>
        </font>
      </p>
      <p>
        <el-row :gutter="20">
          <el-col :span="12" :offset="6"
            ><div>
              <img
                src="@/assets/img/kakeibo1.png"
                alt="Logo"
                class="main__logo1"
              /></div
          ></el-col>
        </el-row>
        <el-row :gutter="20">
          <el-col :span="12" :offset="6"
            ><div>
              <img
                src="@/assets/img/kakeibo2.png"
                alt="Logo"
                class="main__logo1"
              /></div
          ></el-col>
        </el-row>
        <el-row :gutter="20">
          <el-col :span="18" :offset="3"
            ><div>
              <img
                src="@/assets/img/kakeibo3.png"
                alt="Logo"
                class="main__logo1"
              /></div
          ></el-col>
        </el-row>
      </p>


    </el-main>
              <img
                src="@/assets/img/howuse.png"
                alt="Logo"
                class="main__logo1"
              />
    <el-use class="howuse">
      <section>
        <p></p>
        <el-row :gutter="20">
          <el-col :span="20" :offset="2"><h3 class="head4">登録編</h3></el-col>
        </el-row>
        <el-row>
          <el-col :span="8" :offset="3"
            ><div>
              <img
                src="@/assets/img/login.jpg"
                alt="Logo"
                class="main__logo1"
              /></div
          ></el-col>
          <el-col :span="12"
            ><div>
              <h1>まずは、ログインをしよう！</h1>
            </div></el-col
          >
        </el-row>
        <el-row>
          <el-col :span="12"
            ><div><h1>登録が済んでない人は登録から！</h1></div></el-col
          >
          <el-col :span="10"
            ><div>
              <img
                src="@/assets/img/register.jpg"
                alt="Logo"
                class="main__logo1"
              /></div
          ></el-col>
        </el-row>
        <el-row :gutter="20">
          <el-col :span="20" :offset="2"
            ><div class="head4">マイページ編</div></el-col
          >
        </el-row>
        <p></p>
        <el-row>
          <el-col :span="8" :offset="3"
            ><div>
              <img
                src="@/assets/img/ex_Mypage.png"
                alt="Logo"
                class="main__logo1"
              /></div
          ></el-col>
          <el-col :span="12"
            ><div>
              <h1>こちらはホーム画面！</h1>
              <h3>既に登録した画像はここから見れる！</h3>
            </div></el-col
          >
        </el-row>
        <el-row>
          <el-col :span="12"
            ><div><h1>まずは記録をしよう！</h1></div></el-col
          >
          <el-col :span="8"
            ><div>
              <img
                src="@/assets/img/nyuryoku.jpg"
                alt="Logo"
                class="main__logo1"
              /></div
          ></el-col>
        </el-row>
        <el-row>
          <el-col :span="8" :offset="3"
            ><div>
              <img
                src="@/assets/img/ex_table.png"
                alt="Logo"
                class="main__logo1"
              /></div
          ></el-col>
          <el-col :span="12"
            ><div>
              <h1>登録したものを使って行動履歴が見れる！</h1>
            </div></el-col
          >
        </el-row>
        <el-row>
          <el-col :span="12"
            ><div><h1>使ったものをグラフ表示にする事が可能！</h1></div></el-col
          >
          <el-col :span="8"
            ><div>
              <img
                src="@/assets/img/ex_graph.png"
                alt="Logo"
                class="main__logo1"
              /></div
          ></el-col>
        </el-row>
      </section>
    </el-use>
    <el-main>
      <p>
        <font size="10" color="#000000" face="San Francisco UI">
          <i> さぁ、思い出のnikkiをしながらkakeiboを</i>
        </font>
      </p>
    </el-main>

    <el-footer>
      <font size="3" color="#fff" face="San Francisco UI">
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
  background-color: #282a34;
  color: #333;
  text-align: center;
  line-height: 60px;
}
.el-footer {
  background: linear-gradient(#282a34, #282a34);
  color: #333;
  text-align: center;
  line-height: 60px;
}
.head2 {
  background: linear-gradient(
    175deg,
    #c6a0e9 0%,
    #c6a0e9 50%,
    #ece7ec 50%,
    #ece7ec 100%
  );
  color: #333;
  text-align: center;
  line-height: 70px;
}
.head4 {
  background: linear-gradient(
    175deg,
    #3bf0fd 0%,
    #3bf0fd 50%,
    #ece7ec 50%,
    #ece7ec 100%
  );
  color: #333;
  line-height: 30px;
}
.el-main {
  background-color: #ecf0f7;
  color: #333;
  text-align: center;
  line-height: 160px;
}
.howuse {
  background-color: #ecf0f7;
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
.green {
  background: #9ef093;
}

.blue {
  background: #a7f7e9;
}
.main__logo1 {
  width: 100%;
  height: 100%;
}
</style>