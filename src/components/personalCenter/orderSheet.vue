<!-- personalCenter的子组件：用于展示用户的订单 -->

<!-- TODO：根据该用户的订单信息list，实例化orderSheetCard1的list，并展示 -->

<template>
    <el-row class = "orderSheetRowClass">
        <el-col :span="6"><orderSheetCard1/></el-col>
        <el-col :span="6"><orderSheetCard1/></el-col>
        <el-col :span="6"><orderSheetCard1/></el-col>
        <el-col :span="6"><orderSheetCard1/></el-col>
    </el-row>
        <el-row class = "orderSheetRowClass">
        <el-col :span="6"><orderSheetCard1/></el-col>
        <el-col :span="6"><orderSheetCard1/></el-col>
        <el-col :span="6"><orderSheetCard1/></el-col>
        <el-col :span="6"><orderSheetCard1/></el-col>
    </el-row>
</template>

<script>
  import { defineComponent ,ref } from 'vue'
  import { NTag,NButton} from 'naive-ui'
  import orderSheetCard1 from '../cards/orderSheetCard1.vue'

  export default defineComponent({
    components: {
      NTag,
      NButton,
      orderSheetCard1
    },
  })

</script>


