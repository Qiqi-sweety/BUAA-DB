<!-- userOrderPage的子组件:展示该店铺的所有用户评价 -->

<!-- TODO:
1.展示本店铺的所有评价，实例化rateCard1，进行展示 -->

<template>
    <n-card  style="margin-bottom: 50px"  class = "evaluateCardClass">
       <!--评价 -->
      <el-row class = "evaluateRow">
        <el-col :span="12"><rateCard1/></el-col>
        <el-col :span="12"><rateCard1/></el-col>
      </el-row>
    </n-card>
</template>

<script>
  import { defineComponent ,ref } from 'vue'
  import {NCard} from 'naive-ui'
  import rateCard1 from '../cards/rateCard1.vue'

  export default defineComponent({
    components: {
      NCard,
      rateCard1,
    },
  })
  </script>

  <style>
  .evaluateCardClass {
    width: 95%;
    margin-left: auto;
    margin-right: auto;
  }

  .evaluateRow {
    margin-left: 35px;
  }

</style>