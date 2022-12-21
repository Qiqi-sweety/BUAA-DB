<template>
  <el-row>
      <n-button type="warning" style="margin-left:90%;margin-bottom:20px">导出图表</n-button>
  </el-row>
  <el-row>
    <el-table :data="tableData" style="width: 100%">
        <el-table-column prop="No" label="序号" width="180" />
        <el-table-column prop="date" label="订单日期" width="250" />
        <el-table-column prop="store" label="购买用户" width="250"/>
        <el-table-column prop="objects" label="商品内容" width="400"/>
        <el-table-column prop="money" label="总价" />
        <el-table-column prop="rate" label="评分" />
    </el-table>
  </el-row>
</template>

<script>
  import { defineComponent ,ref } from 'vue'
  import { NTag,NButton} from 'naive-ui'
  import rateCard2 from '../cards/rateCard2.vue'

  export default defineComponent({
    components: {
      NTag,
      NButton,
      rateCard2,
    },
  })

</script>