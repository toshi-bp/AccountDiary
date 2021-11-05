<template>

<el-row>
  <el-col :span="4"><div class="grid-content bg-purple-dark">
  ここに、左側の見出し的なものを入れればいいのかなと思っています。いかがでしょうか？
  </div></el-col>
  <el-col :span="20"><div class="grid-content bg-purple-light">

  <el-table
    :data="tableData"
    style="width: 100%"
    max-height="1000">
    <el-table-column
      fixed
      prop="date"
      label="日付"
      width="100">
    </el-table-column>
    <el-table-column
      prop="category"
      label="カテゴリ"
      width="120">
    </el-table-column>
    <el-table-column
      prop="money"
      label="金額"
      width="120">
    </el-table-column>
    <el-table-column
      prop="state"
      label="場所"
      width="120">
    </el-table-column>
    <el-table-column
      prop="photo"
      label="写真"
      width="180">
    </el-table-column>
    <el-table-column
      prop="zip"
      label="Zip"
      width="120">
    </el-table-column>
    <el-table-column
      label="Operations"
      width="120">
      <template v-slot="scope">
        <el-button
          @prevent="deleteRow(scope.$index, tableData)"
          type="text"
          size="small">
          編集
        </el-button>
      </template>
    </el-table-column>
    </el-table>

</div></el-col>
</el-row>



</template>


<style>
  .el-row {
    margin-bottom: 20px;
    /* &:last-child {
      margin-bottom: 0;
    } */
  }
  .el-col {
    border-radius: 4px;
  }
</style>



<script>
  export default {
    data() {
      return {
        tableData: [{
          date: '2016-05-03',
          category: '洋服',
          money: 'California',
          state: 'Los Angeles',
          photo: 'No. 189',
          zip: 'CA 90036'
        }, {
          date: '2016-05-02',
          category: '洋服',
          money: 'California',
          state: 'Los Angeles',
          photo: 'No. 189',
          zip: 'CA 90036'
        }, {
          date: '2016-05-04',
          category: '品物',
          money: 'California',
          state: 'Los Angeles',
          photo: 'No. 189',
          zip: 'CA 90036'
        }, {
          date: '2016-05-01',
          category: 'お手紙',
          money: 'California',
          state: 'Los Angeles',
          photo: 'No. 189',
          zip: 'CA 90036'
        }, {
          date: '2016-05-08',
          category: 'jack',
          money: 'California',
          state: 'Los Angeles',
          photo: 'No. 189',
          zip: 'CA 90036'
        }, {
          date: '2016-05-06',
          category: 'jack',
          money: 'California',
          state: 'Los Angeles',
          photo: 'No. 189',
          zip: 'CA 90036'
        }, {
          date: '2016-05-07',
          category: 'jack',
          money: 'California',
          state: 'Los Angeles',
          photo: 'No. 189',
          zip: 'CA 90036'
        }]
      }
    }
  }
</script>